import os

RAW_DATA = 'Raw_Data'
DATA_FILE_BASE_NAME = 'Daily_Car_Price_Telegram'


KHODROO_ROOZ_HTML_DIR_NAME = 'khodroo_rooz'
KHODROO_ROOZ_HTML_DIR_PATH = os.path.join(RAW_DATA, KHODROO_ROOZ_HTML_DIR_NAME)
HTML_DATA_FILE_BASE_NAME = 'messages_container_'




def get_path(base_dir=RAW_DATA, data_dir_relative_to_base_dir='',
             data_file_base_name=DATA_FILE_BASE_NAME, data_file_name_ext=".txt"):
    return os.path.join(base_dir, data_dir_relative_to_base_dir, data_file_base_name + data_file_name_ext)


if __name__ == '__main__':
    example_data_file_name = 'draft.txt'
    data_path = get_path(base_dir=RAW_DATA, data_file_base_name=DATA_FILE_BASE_NAME)
    example_data_path = get_path(base_dir=RAW_DATA, data_file_base_name=example_data_file_name)
