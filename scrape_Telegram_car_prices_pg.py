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





lines_of_draft = draft_contents.split('\n')


# scraping and adding factory column


# Define the pattern for extracting Jalaali dates, car factories, and car details
pattern = r'📅(.+?)\n([\s\S]*?)(?=\n📅|$)'

# Extract Jalaali dates, car factories, and car details from the text
matches = re.findall(pattern, draft_file_name)

# Create a table
table = PrettyTable()
table.field_names = ['Jalaali Date', 'Factory', 'Car Type', 'Car Price']

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
    car_factory = None  # Initialize the car factory for each day
    lines = car_info.strip().split('\n')
    for line in lines:
        if line.startswith('🔱'):
            car_factory = line.strip('🔱 ')
        else:
            car_type_price = re.findall(r'(.+?)⬅️([\d۰۱۲۳۴۵۶۷۸۹,]+)', line)
            if car_type_price:
                car_type, car_price = car_type_price[0]
                car_type = convert_persian_numbers(car_type.strip())
                car_price = car_price.strip().replace(',', '')
                table.add_row([date.strip(), car_factory, car_type, car_price])

# Print the table
print(table)




