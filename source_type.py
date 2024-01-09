SOURCE_TYPES = {}


class SourceType:
    def __init__(self, name=None, project_abv=None, parent_source=None, base_url=None):
        self.name = name
        self.project_abv = project_abv
        self.parent_source = parent_source
        self.base_url = base_url
        self.add_to_SOURCE_TYPES()

    def add_to_SOURCE_TYPES(self):
        SOURCE_TYPES[self.name] = self


TELEGRAM_CHANNEL = SourceType(name='Telegram_Channel', project_abv='TC',
                              parent_source='Telegram', base_url='https://t.me')
