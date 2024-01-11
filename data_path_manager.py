import os

PROJECT_ROOT_NAME = 'data_extraction'
PROJECT_ROOT_PATH = '/home/jvn/GameTheorist/Computing/PythonProjects/data_extraction'

DATA_BASE_DIR = 'Data'
RAW_DATA_BASE_DIR_NAME = 'Raw_Data'
PROCESSED_DATA_DIR_NAME = 'Processed_Data'


DATA_FILE_BASE_NAME = 'Daily_Car_Price_Telegram'


KHODROO_ROOZ_HTML_DIR_NAME = 'khodroo_rooz'
KHODROO_ROOZ_HTML_DIR_PATH = os.path.join(RAW_DATA_BASE_DIR_NAME, KHODROO_ROOZ_HTML_DIR_NAME)
HTML_DATA_FILE_BASE_NAME = 'messages_container_'


class PathConfig:
    def __init__(self, project_root_name=PROJECT_ROOT_NAME,
                 project_root_path_abs=PROJECT_ROOT_PATH,
                 data_base_dir_name=DATA_BASE_DIR,
                 raw_data_base_dir_name=RAW_DATA_BASE_DIR_NAME,
                 processed_data_dir_name=PROCESSED_DATA_DIR_NAME,
                 data_base_root_path_rel='',
                 structure='STANDARD_TREE'):
        self.project_root_name = project_root_name
        self.project_root_path_abs = project_root_path_abs
        self.data_base_dir_name = data_base_dir_name
        self.raw_data_base_dir_name = raw_data_base_dir_name
        self.processed_data_dir_name = processed_data_dir_name
        self.structure = structure
        self.data_base_root_path_rel = data_base_root_path_rel
        if self.structure == 'STANDARD_TREE':
            self.data_base_dir_path_rel = os.path.join(self.data_base_root_path_rel, self.data_base_dir_name)
            self.raw_data_base_dir_path_rel = os.path.join(self.data_base_dir_name, self.raw_data_base_dir_name)
            self.processed_data_dir_path_rel = os.path.join(self.data_base_dir_name, self.processed_data_dir_name)

    def check_project_path(self, print_warnings_regardless=False):
        if (os.getcwd() != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from current directory')
            print(f'Parent of Current Working Directory Is {os.path.dirname(os.getcwd())}')
            print(f'Project Root Path Is {self.project_root_path_abs}')
        if (os.path.dirname(__file__) != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from directory of current file')
            print(f'Directory of Current file Is {os.path.dirname(__file__) }')
            print(f'Project Root Path Is {self.project_root_path_abs}')
        else:
            print('Paths related to Project Root seems to be correct')


DEFAULT_PATH_CONFIG = PathConfig()


def get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_dir_relative_to_base_dir='',
             data_file_base_name=DATA_FILE_BASE_NAME, data_file_name_ext=".txt"):
    return os.path.join(base_dir, data_dir_relative_to_base_dir, data_file_base_name + data_file_name_ext)


if __name__ == '__main__':
    example_data_file_name = 'draft.txt'
    data_path = get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_file_base_name=DATA_FILE_BASE_NAME)
    example_data_path = get_path(base_dir=RAW_DATA_BASE_DIR_NAME, data_file_base_name=example_data_file_name)
