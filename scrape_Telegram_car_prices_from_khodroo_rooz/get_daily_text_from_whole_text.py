import re
import pandas as pd

import data_path_manager
import data_source

def separate_whole_raw_text_to_daily_raw_text(date_sign='📅', pattern=None, content=data_contents):
    """
    :param content:
    :param date_sign:
    :param pattern:
           default value is fr'{date_sign}(.+?)\n([\s\S]*?)(?=\n{date_sign}|$)'

    """
    if pattern is None:
        pattern = fr'{date_sign}(.+?)\n([\s\S]*?)(?=\n{date_sign}|$)'

    return re.findall(pattern, content)









