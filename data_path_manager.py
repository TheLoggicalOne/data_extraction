import os

PROJECT_ROOT_NAME = 'data_extraction'
PROJECT_ROOT_PATH = '/home/jvn/GameTheorist/Computing/PythonProjects/data_extraction'
# See PathConfig check_project_path, we need a more consistent way of getting project root path.
# maybe a file that we are always sure is in project first level will do the trick
DATA_BASE_DIR = 'Data'
RAW_DATA_BASE_DIR_NAME = 'Raw_Data'
PROCESSED_DATA_DIR_NAME = 'Processed_Data'
FINAL_DATA_DIR_NAME = 'Final_Data'




class PathConfig:
    def __init__(self, project_root_name=PROJECT_ROOT_NAME,
                 project_root_path_abs=PROJECT_ROOT_PATH,
                 data_base_dir_name=DATA_BASE_DIR,
                 raw_data_base_dir_name=RAW_DATA_BASE_DIR_NAME,
                 processed_data_dir_name=PROCESSED_DATA_DIR_NAME,
                 final_data_dir_name=FINAL_DATA_DIR_NAME,
                 data_base_root_path_rel='',
                 structure='STANDARD_TREE'):
        self.project_root_name = project_root_name
        self.project_root_path_abs = project_root_path_abs
        self.data_base_dir_name = data_base_dir_name
        self.raw_data_base_dir_name = raw_data_base_dir_name
        self.processed_data_dir_name = processed_data_dir_name
        self.final_data_dir_name = final_data_dir_name
        self.structure = structure
        self.data_base_root_path_rel = data_base_root_path_rel
        if self.structure == 'STANDARD_TREE':
            self.data_base_dir_path_rel = os.path.join(self.data_base_root_path_rel, self.data_base_dir_name)
            self.raw_data_base_dir_path_rel = os.path.join(self.data_base_dir_path_rel, self.raw_data_base_dir_name)
            self.processed_data_dir_path_rel = os.path.join(self.data_base_dir_path_rel, self.processed_data_dir_name)
            self.final_data_dir_path_rel = os.path.join(self.data_base_dir_path_rel, self.final_data_dir_name)

    def check_project_path(self, print_warnings_regardless=False):
        if (os.getcwd() != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from current directory')
            print(f'Current Working Directory Is {os.getcwd()}')
            print(f'Project Root Path Is {self.project_root_path_abs}')
        if (os.path.dirname(__file__) != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from directory of current file')
            print(f'Directory of Current file Is {os.path.dirname(__file__) }')
            print(f'Project Root Path Is {self.project_root_path_abs}')
            print(f'Path of Current file Is {__file__}')
        else:
            print('Paths related to Project Root seems to be correct')


DEFAULT_PATH_CONFIG = PathConfig()


if __name__ == '__main__':
    pass
