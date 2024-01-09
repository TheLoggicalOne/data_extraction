import re
import pandas as pd
from prettytable import PrettyTable

import data_path_manager

# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

# set up path of files and folders
example_data_file_name = 'draft.txt'
data_path = data_manager.get_path(base_dir=data_manager.RAW_DATA,
                                  data_file_base_name=data_manager.DATA_FILE_BASE_NAME,
                                  data_file_name_ext='_20230107.txt')
example_data_path = data_manager.get_path(base_dir=data_manager.RAW_DATA,
                                          data_file_base_name=example_data_file_name)

# read the data
with open(example_data_path, "r") as file:
    draft_contents = file.read()

with open(data_path, "r") as file:
    data_contents = file.read()

# ---------------------------------------------------------------------------------------------------------------------#
# --------------------------- EXTRACTING DATA FROM EXAMPLE CONTENT OF @khodroo_rooz -----------------------------------#

# scrapping for draft_content from

# Define the pattern for extracting Jalaali dates and all car info between to consecutive dates
date_in_text_pattern = r'📅(.+?)\n([\s\S]*?)(?=\n📅|$)'
# This re working depends on the fact that each Jalali dates has a '📅' marker and is in separate line
# and  car prices info are between two  to separate lines

# Extract Jalaali dates and car prices info of each day from the text
matches = re.findall(date_in_text_pattern, draft_contents)


# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

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


def get_car_prices_info_from_daily_raw_text(raw_text_of_daily_car_price_info=None, pattern=None,
                                            price_name_separator='⬅️'):
    if pattern is None:
        pattern = fr'(.+?){price_name_separator}([\d۰۱۲۳۴۵۶۷۸۹,]+)'
    car_price_info = re.findall(r'(.+?)⬅️([\d۰۱۲۳۴۵۶۷۸۹,]+)', raw_text_of_daily_car_price_info)
    return car_price_info


def get_car_prices_info_with_factory_from_daily_raw_text(raw_text_of_daily_car_price_info=None, pattern=None,
                                                         price_name_separator='⬅️', factory_sign='🔱'):
    l = []
    if pattern is None:
        pattern = fr'(.+?){price_name_separator}([\d۰۱۲۳۴۵۶۷۸۹,]+)'
    car_factory = None
    lines = raw_text_of_daily_car_price_info.split('\n')
    for line in lines:
        if line.startswith(factory_sign):
            car_factory = line.strip(factory_sign)
        else:
            car_type_price = re.findall(pattern, line)
            if car_type_price:
                car_type, car_price = car_type_price[0]
                l.append((car_type, car_price, car_factory))
    return l


def create_daily_car_prices_list_from_whole_text_of_khodroo_rooz(content=data_contents):
    l = []
    for date, raw_text in separate_whole_raw_text_to_daily_raw_text(content=content):
        for car_type, car_price in get_car_prices_info_from_daily_raw_text(raw_text):
            l.append((date, car_type, car_price))

    return l


def create_daily_car_prices_list_with_carfactory_from_whole_text_of_khodroo_rooz(content=data_contents):
    l = []
    for date, raw_text in separate_whole_raw_text_to_daily_raw_text(content=content):
        for car_type, car_price, car_factory in get_car_prices_info_with_factory_from_daily_raw_text(raw_text):
            l.append((date, car_type, car_price, car_factory))
    return l


# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

list_of_daily_car_prices_info = create_daily_car_prices_list_from_whole_text_of_khodroo_rooz(
    content=data_contents)
list_of_daily_car_prices_info_example = create_daily_car_prices_list_from_whole_text_of_khodroo_rooz(
    content=draft_contents)

dict_of_daily_car_price_info_example = {date: [(date, car_type, car_price) for car_type, car_price in
                                               get_car_prices_info_from_daily_raw_text(raw_text)] for date, raw_text in
                                        separate_whole_raw_text_to_daily_raw_text(
                                            content=draft_contents)}
dict_keys = list(dict_of_daily_car_price_info_example.keys())

# ---------------------------------------------------------------------------------------------------------------------#
# --------------------------------------- CREATING TABLES USING Pandas ------------------------------------------------#

daily_car_price_info_df_example = pd.DataFrame(list_of_daily_car_prices_info_example, columns=['Jalaali Date',
                                                                                               'Car Type', 'Car Price'])

daily_car_price_info_df = pd.DataFrame(list_of_daily_car_prices_info, columns=['Jalaali Date', 'Car Type', 'Car Price'])

daily_car_price_info_with_factory_df = pd.DataFrame(
    create_daily_car_prices_list_with_carfactory_from_whole_text_of_khodroo_rooz(content=data_contents),
    columns=['Jalaali Date', 'Car Type', 'Car Price', 'car_factory'])

# ---------------------------------------------------------------------------------------------------------------------#
# -------------------------------------- CREATING TABLES USING PrettyTable() ------------------------------------------#

# Create a table
my_table = PrettyTable()
my_table.field_names = ['Jalaali Date', 'Car Type', 'Car Price']

# Add rows to the table
for row in list_of_daily_car_prices_info_example:
    my_table.add_row(list(row))

print(my_table)

# Question: Why are table titles misplaced? because farsi text directions?

# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#
