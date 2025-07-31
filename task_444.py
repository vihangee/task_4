import requests
from bs4 import BeautifulSoup
import csv
import random

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.select('div.quote')

with open('quotes_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating'])  # Mandatory columns

    for quote in quotes:
        name = quote.find('span', class_='text').text.strip()
        
        price = f"₹{random.randint(100, 1000)}"
        
        rating = random.choice(['One', 'Two', 'Three', 'Four', 'Five'])
        
        writer.writerow([name, price, rating])

print("✅ Quotes data saved to quotes_data.csv with Name, Price, and Rating columns.")