class DataSource:
    def __init__(self, name=None, source_type=None, source_id=None, source_desc=None, raw_data_dir_path=None, url=None,
                 project_id=None):
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

    def create_project_id(self):
        if self.source_type is TELEGRAM_CHANNEL:
            return self.name + '_' + 'TC'


TELEGRAM_CHANNEL = 'Telegram_Channel'
