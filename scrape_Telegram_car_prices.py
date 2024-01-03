import os
import re
from prettytable import PrettyTable

import data_manager
from persian_text_tools import convert_persian_numbers

# set up path of files and folders
example_data_file_name = 'draft.txt'
data_path = data_manager.get_path(base_dir=data_manager.RAW_DATA,
                                  data_file_base_name=data_manager.DATA_FILE_BASE_NAME)
example_data_path = data_manager.get_path(base_dir=data_manager.RAW_DATA,
                                          data_file_base_name=example_data_file_name)

# read the data
with open(example_data_path, "r") as file:
    draft_contents = file.read()

with open(data_path, "r") as file:
    data_contents = file.read()

# scrapping for draft_content from

# Define the pattern for extracting Jalaali dates and all car info between to consecutive dates
pattern = r'📅(.+?)\n([\s\S]*?)(?=\n📅|$)'
# This re working depends on the fact that each Jalali dates has a '📅' marker and is in separate line
# and  car prices info are between two  to separate lines

# Extract Jalaali dates and car prices info of each day from the text
matches = re.findall(pattern, draft_contents)

# Create a table
table = PrettyTable()
table.field_names = ['Jalaali Date', 'Car Type', 'Car Price']


# Add rows to the table
for date, car_info in matches:
    car_details = re.findall(r'(.+?)⬅️([\d۰۱۲۳۴۵۶۷۸۹,]+)', car_info)
    for car_type, car_price in car_details:
        # uncomment/comment following two lines to convert persian to english numbers
        # car_type = convert_persian_numbers(car_type.strip())
        car_type = car_type.strip()

        car_price = car_price.strip().replace(',', '')
        table.add_row([date.strip(), car_type, car_price])

# Print the table
print(table)

# wtf = '📅'

lines_of_draft = draft_contents.split('\n')


# Question: Why are table titles misplaced? because farsi text directions?