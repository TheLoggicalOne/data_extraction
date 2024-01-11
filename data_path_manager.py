import os

DATA_BASE_DIR = 'Data'
RAW_DATA_BASE_DIR_NAME = 'Raw_Data'
PROCESSED_DATA_DIR_NAME = 'Processed_Data'


DATA_FILE_BASE_NAME = 'Daily_Car_Price_Telegram'


KHODROO_ROOZ_HTML_DIR_NAME = 'khodroo_rooz'
KHODROO_ROOZ_HTML_DIR_PATH = os.path.join(RAW_DATA_BASE_DIR_NAME, KHODROO_ROOZ_HTML_DIR_NAME)
HTML_DATA_FILE_BASE_NAME = 'messages_container_'


class PathConfig:
    def __init__(self, data_base_dir_name, raw_data_base_dir_name, processed_data_dir_name,
                 root='',
                 structure='STANDARD_TREE'):
        self.data_base_dir_name = data_base_dir_name
        self.raw_data_base_dir_name = raw_data_base_dir_name
        self.processed_data_dir_name = processed_data_dir_name
        self.structure = structure
        self.root = root
        if self.structure == 'STANDARD_TREE':
            self.data_base_dir_path = os.path.join(self.root, self.data_base_dir_name)
            self.raw_data_base_dir_path = os.path.join(self.data_base_dir_name, self.raw_data_base_dir_name)
            self.processed_data_dir_path = os.path.join(self.data_base_dir_name, self.processed_data_dir_name)


DEFAULT_PATH_CONFIG = PathConfig( data_base_dir_name=DATA_BASE_DIR,
                                  raw_data_base_dir_name=RAW_DATA_BASE_DIR_NAME,
                                  processed_data_dir_name=PROCESSED_DATA_DIR_NAME)


def get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_dir_relative_to_base_dir='',
             data_file_base_name=DATA_FILE_BASE_NAME, data_file_name_ext=".txt"):
    return os.path.join(base_dir, data_dir_relative_to_base_dir, data_file_base_name + data_file_name_ext)


if __name__ == '__main__':
    example_data_file_name = 'draft.txt'
    data_path = get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_file_base_name=DATA_FILE_BASE_NAME)
    example_data_path = get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_file_base_name=example_data_file_name)
