class DataSource:
    def __init__(self, name=None, source_type=None, source_id=None, raw_data_path=None,  url=None):
        self.name = name
        self.source_type = source_type
        if source_id is None:
            self.source_id = self.name
        else:
            self.source_id = source_id
        if raw_data_path is None:
            self.raw_data_path = self.source_id
        else:
            self.raw_data_path = raw_data_path
        self.url = url
