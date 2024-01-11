import os

import data_path_manager
from source_type import SOURCE_TYPES, SourceType


class DataSource:
    
    def __init__(self, name=None, source_type=None, source_id=None, source_desc=None, data_dir_name=None,
                 data_dir_path=None, url=None, project_id=None,
                 project_path_config=data_path_manager.DEFAULT_PATH_CONFIG):
        self.name = name
        self.source_type = source_type
        self.complete_source_type()
        if source_id is None:
            self.source_id = self.name
        else:
            self.source_id = source_id
        self.source_desc = source_desc

        if project_id is None:
            self.project_id = self.create_project_id()
        else:
            self.project_id = project_id

        if data_dir_name is None:
            self.data_dir_name = self.project_id
        else:
            self.data_dir_name = data_dir_name


        self.project_path_config = project_path_config

        self.data_dir_path = data_dir_path

        self.url = url

    def create_project_id(self):
        try:
            r = self.source_type.project_abv
        except Exception as error:
            print(f'Error:  "{error}"')
            print(f'Error type: "{type(error)}"')
            r = ''
        return self.name + '_' + r

    def complete_source_type(self):
        if isinstance(self.source_type, str):
            try:
                self.source_type = SOURCE_TYPES[self.source_type]
            except KeyError as error:
                print(f'Error: "{error}"')
                print(f'Error type: "{type(error)}"')
                print(f'Complete the source type "{self.source_type}" in source_type.py module by creating SourceType')

    def abs_path_from_cwd(self):
        return


if __name__ == '__main__':
    test_source = DataSource(name='khodroo_rooz',
                             source_type='Telegram',
                             source_id='@khodroo_rooz',
                             source_desc="""Telegram Channel with almost always one message per day 
                                           containing daily new car prices gathered from car dealers and sellers""",
                             url='t.me/khodroo_rooz')
