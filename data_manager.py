import os

RAW_DATA = 'Raw_Data'
DATA_FILE_BASE_NAME = 'Daily_Car_Price_Telegram.txt'


def get_path(base_dir=RAW_DATA, data_file_base_name=DATA_FILE_BASE_NAME, data_file_name_ext=""):
    return os.path.join(base_dir, data_file_base_name+data_file_name_ext)



example_data_file_name = 'draft.txt'
data_path = get_path(base_dir=RAW_DATA, data_file_base_name=DATA_FILE_BASE_NAME)
example_data_path = get_path(base_dir=RAW_DATA, data_file_base_name=example_data_file_name)
