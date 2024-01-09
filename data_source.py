from source_type import SOURCE_TYPES, SourceType


class DataSource:
    def __init__(self, name=None, source_type=None, source_id=None, source_desc=None, raw_data_dir_path=None,
                 url=None, project_id=None):
        self.name = name
        self.source_type = source_type

        if source_id is None:
            self.source_id = self.name
        else:
            self.source_id = source_id
        self.source_desc = source_desc

        if project_id is None:
            self.project_id = self.create_project_id()
        else:
            self.project_id = project_id

        if raw_data_dir_path is None:
            self.raw_data_path = self.project_id
        else:
            self.raw_data_path = raw_data_dir_path

        self.url = url

        self.complete_source_type()

    def create_project_id(self):
        if self.source_type is 'Telegram_Channel':
            return self.name + '_' + 'TC'

    def complete_source_type(self):
        if isinstance(self.source_type, str):
            try:
                self.source_type = SOURCE_TYPES[self.source_type]
            except KeyError as error:
                print(f'Error is {error}')
                print(f'Error type is {type(error)}')
                print(f'Complete the source type "{self.source_type}" in source_type.py module by creating SourceType')




if __name__ == '__main__':
    test_source = DataSource(name='khodroo_rooz',
                                           source_type='Telegram',
                                           source_id='@khodroo_rooz',
                                           source_desc="""Telegram Channel with almost always one message per day 
                                           containing daily new car prices gathered from car dealers and sellers""",
                                           url='t.me/khodroo_rooz')

