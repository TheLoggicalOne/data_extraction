import os
import re
from prettytable import PrettyTable
# set up path of files and folders
Raw_Data = 'Raw_Data'
data_file_name = 'Daily_Car_Price_Telegram.txt'
draft_file_name = 'draft.txt'
data_path = os.path.join(Raw_Data, data_file_name)
draft_path = os.path.join(Raw_Data, draft_file_name)


# read the data
with open(draft_path, "r") as file:
    draft_contents = file.read()

with open(draft_path, "r") as file:
    data_contents = file.read()




# scrapping for draft_content from
# Define the pattern for extracting Jalaali dates and car details


pattern = r'📅(.+?)\n([\s\S]*?)(?=\n📅|$)'

# Extract Jalaali dates and car details from the text
matches = re.findall(pattern, draft_contents)

# Create a table
table = PrettyTable()
table.field_names = ['Jalaali Date', 'Car Type', 'Car Price']

# Helper function to convert Persian numbers to English numbers
def convert_persian_numbers(text):
    persian_to_english = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9'
    }
    return ''.join(persian_to_english.get(char, char) for char in text)

# Add rows to the table
for date, car_info in matches:
    car_details = re.findall(r'(.+?)⬅️([\d۰۱۲۳۴۵۶۷۸۹,]+)', car_info)
    for car_type, car_price in car_details:

        #uncomment/comment following two lines to convert persian to english numbers
        # car_type = convert_persian_numbers(car_type.strip())
        car_type = car_type.strip()

        car_price = car_price.strip().replace(',', '')
        table.add_row([date.strip(), car_type, car_price])

# Print the table
print(table)


# wtf = '📅'

lines_of_draft = draft_contents.split('\n')

