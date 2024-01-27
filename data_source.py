import os

import data_path_manager
from source_type import SOURCE_TYPES, SourceType


class DataSource:
    """Represents a data source.

    This class provides functionality to handle data sources. Its main job is gathering and holding information about
    a given data source and providing easy access to these information.  It includes methods to create a project ID and
    complete the source type. The attributes listed below are initialized through the constructor (`__init__`).

    Attributes:
        name (str): The name of the data source in the project
        source_type (SourceType): The type of the data source.
        source_id (str): The ID of the data source (default: same as `name`).
        source_desc (str): The description of the data source.
        data_dir_name (str): The name of the data directory (default: same as `project_id`).
        data_dir_path (str): The path to the data directory.
        url (str): The URL of the data source.
        project_id (str): The project ID of the data source (default: created using `name` and `source_type`).
        project_path_config (str): The path configuration for the project (default: data_path_manager.DEFAULT_PATH_CONFIG).
    """

    def __init__(self, name=None, source_type=None, source_id=None, source_desc=None, data_dir_name=None,
                 data_dir_path=None, url=None, project_id=None,
                 project_path_config=data_path_manager.DEFAULT_PATH_CONFIG):
        """Initialize a DataSource object.

        Args:
            name (str): The name of the data source.
            source_type (str or SourceType): The type of the data source.
            source_id (str, optional): The ID of the data source. Defaults to None.
            source_desc (str, optional): The description of the data source. Defaults to None.
            data_dir_name (str, optional): The name of the data directory. Defaults to None.
            data_dir_path (str, optional): The path to the data directory. Defaults to None.
            url (str, optional): The URL of the data source. Defaults to None.
            project_id (str, optional): The project ID of the data source. Defaults to None.
            project_path_config (str, optional): The path configuration for the project. Defaults to
                data_path_manager.DEFAULT_PATH_CONFIG.
        """
        self.name = name
        self.source_type = source_type
        self.complete_source_type()
        # if source_id is None:
        #     self.source_id = self.name
        # else:
        #     self.source_id = source_id
        self.source_id = source_id or self.name
        self.source_desc = source_desc

        # if project_id is None:
        #     self.project_id = self.create_project_id()
        # else:
        #     self.project_id = project_id
        self.project_id = project_id or self.create_project_id()
        # if data_dir_name is None:
        #     self.data_dir_name = self.project_id
        # else:
        #     self.data_dir_name = data_dir_name
        self.data_dir_name = data_dir_name or self.project_id
        self.project_path_config = project_path_config

        self.data_dir_path = data_dir_path

        self.url = url

    def create_project_id(self):
        try:
            r = self.source_type.project_abv
        except Exception as error:
            print(f'Project Warning:  "{error}"')
            print(f'Error type: "{type(error)}"')
            r = ''
        return self.name + '_' + r

    def complete_source_type(self):
        if isinstance(self.source_type, str):
            try:
                self.source_type = SOURCE_TYPES[self.source_type]
            except KeyError as error:
                print(f'Project Warning: "{error}"')
                print(f'Error type: "{type(error)}"')
                print(f'Complete the source type "{self.source_type}" in source_type.py module by creating SourceType')

    def get_data_path(self, content_type=None,  path_config: data_path_manager.PathConfig = None,
                      data_type_override=None,
                      data_file_name_override=None, data_file_ext_override=None):
        if path_config is None:
            path_config = self.project_path_config
        if data_type in path_config.data_types:
            middle_path_rel = path_config.path_rel_of_data_type_dict[data_type]

        elif data_type is None:
            middle_path_rel = path_config.data_base_dir_path_rel


        path_ = os.path.join(path_config.project_root_path_abs,
                             middle_path_rel,
                             self.data_dir_name, data_file_name + data_file_ext)
        return path_



if __name__ == '__main__':
    test_source = DataSource(name='khodroo_rooz',
                             source_type='Telegram',
                             source_id='@khodroo_rooz',
                             source_desc="""Telegram Channel with almost always one message per day 
                                           containing daily new car prices gathered from car dealers and sellers""",
                             url='t.me/khodroo_rooz')

    p = __file__
    c = os.getcwd()
    d = data_path_manager.DEFAULT_PATH_CONFIG
