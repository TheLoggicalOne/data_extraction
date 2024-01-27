import datetime


class ContentType:
    def __init__(self, name=None, base_file_system_rep=None, data_type=None, file_ext=None,
                 naming_ext_convention_key='standard_from_start_to_end'):
        self.name = name

        self.base_file_system_rep = base_file_system_rep or self.name
        self.data_type = data_type


        self.file_ext = file_ext or self.get_file_ext_from_data_type()
        self.naming_ext_convention_key = naming_ext_convention_key

    def add_naming_ext(self, *args, base_fs_name=None, naming_convention_key=None, **kwargs):
        if base_fs_name is None:
            base_fs_name = self.base_file_system_rep
        if naming_convention_key is None:
            naming_convention_key = self.naming_ext_convention_key
        print(args)
        print(kwargs)
        return NAMING_EXT_CONVENTIONS[naming_convention_key](base_fs_name, *args, **kwargs)

    def get_file_ext_from_data_type(self, dtype=None):
        final_dtype = dtype or self.data_type
        return FILE_EXT_OF_DTYPES[final_dtype]


FILE_EXT_OF_DTYPES = {'text': '.txt', 'html': '.html'}
NAMING_EXT_CONVENTIONS = {'standard_from_start_to_end': lambda name, start_, end_: '_'.join([name, 'from', start_,
                                                                                             'to', end_])
                          }

if __name__ == '__main__':
    ct = ContentType(name='whole_text_of_all_messages', data_type='text', file_ext='.txt')
