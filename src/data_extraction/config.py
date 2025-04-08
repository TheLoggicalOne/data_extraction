import json
import os


# we are assuming config.py is in ROOT_DIR/src/data_extraction and config.json is(or should be) in ROOT_DIR
# So we Get the root directory by navigating up from the current file's directory twice
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

CONFIG_FILE = os.path.join(ROOT_DIR, "config.json")
TEMP_CONFIG_FILE = CONFIG_FILE + ".tmp"



# default config keys, grouping them by their purpose
DEFAULT_CONFIG = {
    "telegram": {
        "TELEGRAM_API_ID": None,
        "TELEGRAM_API_HASH": None,
    },
    "database": {
        "DATABASE_URI": None,
    },
    "logging": {
        "LOG_LEVEL": "INFO"
    }
}

def load_configuration(required_keys=None, config_group=None):
    """
    Load configuration for specific keys or groups , prompt for missing values.
    
    Args:
        required_keys (list): Specific keys to load (ignores `config_group` if provided).
        config_group (str): Specific group to load keys from (if `required_keys` is None).
    
    Returns:
        dict: Configuration containing the requested keys.
    """
    config = {}

    # Step 1: Load existing config
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                config = json.load(file)
        except json.JSONDecodeError:
            print("Error: Corrupted configuration file. Recreating it.")
            config = {}

    # Step 2: Determine required keys to validate
    if required_keys:
        required_config = {key: None for key in required_keys}
    elif config_group and config_group in DEFAULT_CONFIG:
        required_config = DEFAULT_CONFIG[config_group]
    else:
        raise ValueError("You must specify either `required_keys` or a valid `config_group`.")

    # Step 3: Validate and fill missing keys
    for key, default_value in required_config.items():
        if key not in config or config[key] is None:
            config[key] = prompt_user_for_key(key, default_value)

    # Step 4: Save the updated configuration
    save_configuration(config)
    return config

def prompt_user_for_key(key, default_value):
    """Prompt the user for a specific key value."""
    user_input = input(f"Enter value for {key} (default: {default_value}): ")
    return user_input.strip() if user_input else default_value

def save_configuration(config):
    """Save the updated configuration safely to avoid data corruption."""
    try:
        # Write to a temporary file first
        with open(TEMP_CONFIG_FILE, "w") as temp_file:
            json.dump(config, temp_file, indent=4)

        # Replace the original file with the temporary file
        os.replace(TEMP_CONFIG_FILE, CONFIG_FILE)
        print(f"Configuration saved to {CONFIG_FILE}.")
    except Exception as e:
        print(f"Error saving configuration: {e}")
        if os.path.exists(TEMP_CONFIG_FILE):
            os.remove(TEMP_CONFIG_FILE)
        raise


if __name__ == "__main__":
    # Example usage
    telegram_config = load_configuration(config_group="telegram")
    # database_config = load_configuration(config_group="database")
    # log_level = load_configuration(required_keys=["LOG_LEVEL"])["LOG_LEVEL"]

    print(f"Telegram API ID: {telegram_config['TELEGRAM_API_ID']}")
    # print(f"Database URI: {database_config['DATABASE_URI']}")
    # print(f"Log Level: {log_level}")
