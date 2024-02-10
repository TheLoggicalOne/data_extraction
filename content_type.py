"""
To describe and manage different kinds of file contents and their naming conventions
currently neither of SourceType and DataSource holds this info, which kind of make sense since these could have more
than one ContentType

"""

import datetime


class ContentType:
    def __init__(self, name=None, base_file_system_rep=None, data_format=None, file_ext=None,
                 naming_ext_convention_key='standard_from_start_to_end'):
        self.name = name

        self.base_file_system_rep = base_file_system_rep or self.name
        self.data_format = data_format


        self.file_ext = file_ext or self.get_file_ext_from_data_format()
        self.naming_ext_convention_key = naming_ext_convention_key

    def add_naming_ext(self, *args, base_fs_name=None, naming_convention_key=None, **kwargs):
        if base_fs_name is None:
            base_fs_name = self.base_file_system_rep
        if naming_convention_key is None:
            naming_convention_key = self.naming_ext_convention_key
        print(args)
        print(kwargs)
        return NAMING_EXT_CONVENTIONS[naming_convention_key](base_fs_name, *args, **kwargs)

    def get_file_ext_from_data_format(self, dformat=None):
        final_dformat = dformat or self.data_format
        return FILE_EXT_OF_DFORMAT[final_dformat]


FILE_EXT_OF_DFORMAT = {'text': '.txt', 'html': '.html'}
NAMING_EXT_CONVENTIONS = {'standard_from_start_to_end': lambda name_, start_, end_: '_'.join([name_, 'from', start_,
                                                                                             'to', end_])
                          }



if __name__ == '__main__':
    ct = ContentType(name='whole_text_of_all_messages', data_format='text', file_ext='.txt')
