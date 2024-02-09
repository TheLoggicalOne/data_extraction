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
                 data_types=None,
                 dir_name_of_data_type_dict=None,
                 data_base_root_path_rel='',
                 structure='STANDARD_TREE'):
        self.project_root_name = project_root_name
        self.project_root_path_abs = project_root_path_abs
        self.data_base_dir_name = data_base_dir_name

        # if data_types is None:
        #     self.data_types = ['', 'Raw', 'Processed', 'Final']
        # else:
        #     self.data_types = data_types
        self.data_types = data_types or ['', 'Raw', 'Processed', 'Final']

        # if dir_name_of_data_type_dict is None:
        #     self.dir_name_of_data_type_dict = {x: x + '_Data' for x in self.data_types}
        # else:
        #     self.dir_name_of_data_type_dict = dir_name_of_data_type_dict
        self.dir_name_of_data_type_dict = dir_name_of_data_type_dict or {x: 'Data_' + x for x in self.data_types}
        self.structure = structure
        self.data_base_root_path_rel = data_base_root_path_rel
        if self.structure == 'STANDARD_TREE':
            self.data_base_dir_path_rel = os.path.join(self.data_base_root_path_rel, self.data_base_dir_name)
            # change next attr to a func that...wait...do we really need them?
            # data_base_dir_name,  dir_name_of_data_type, DataSource_dir_name, content_type_dir_name, file_name
            # self.path_rel_of_data_type_dict = {
            #     x: os.path.join(self.data_base_dir_path_rel, self.dir_name_of_data_type_dict[x])
            #     for x in self.data_types}
            # self.path_rel_frame_of_data_type = {
            #     x: lambda name: os.path.join(self.data_base_dir_path_rel, name, self.dir_name_of_data_type_dict[x])
            #     for x in self.data_types}

    def check_project_path(self, print_warnings_regardless=False):
        if (os.getcwd() != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from current directory')
            print(f'Current Working Directory Is {os.getcwd()}')
            print(f'Project Root Path Is {self.project_root_path_abs}')
        if (os.path.dirname(__file__) != self.project_root_path_abs) or print_warnings_regardless:
            print('Project Warning: project root path is different from directory of current file')
            print(f'Directory of Current file Is {os.path.dirname(__file__)}')
            print(f'Project Root Path Is {self.project_root_path_abs}')
            print(f'Path of Current file Is {__file__}')
        else:
            print('Paths related to Project Root seems to be correct')

    def add_dtype_with_update(self, **dtypes):
        for key, value in dtypes.items():
            self.data_types.append(key)
            self.dir_name_of_data_type_dict[key] = value
            # self.path_rel_of_data_type_dict[key] = os.path.join(
            #     self.data_base_dir_path_rel, self.dir_name_of_data_type_dict[key])


DEFAULT_PATH_CONFIG = PathConfig()

if __name__ == '__main__':
    d = DEFAULT_PATH_CONFIG
