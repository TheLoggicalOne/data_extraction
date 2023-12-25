import requests
from bs4 import BeautifulSoup

url = "https://asbe-bokhar.com/car-price/daily-car-price/"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the car prices
# table = soup.find('wp-block-table is-style-regular')
#
all_tables_soup = soup.find_all('figure', class_="wp-block-table is-style-regular")
#
#
table = all_tables_soup.pop(0)
#
# # Extract the data from the table
car_prices = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) >= 2:
        car_model = columns[0].text.strip()
        car_price = columns[1].text.strip()
        car_price_2 = columns[2].text.strip()
        car_prices.append((car_model, car_price, car_price_2))

# Print the car prices
for car in car_prices:
    print(f"Car Model: {car[0]}, Price: {car[1]}")


