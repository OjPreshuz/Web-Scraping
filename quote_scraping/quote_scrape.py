from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'http://quotes.toscrape.com'
all_quotes = []

for page in range(1, 11):
    url = f'{base_url}/page/{page}'
    quotes = requests.get(url)
    quotes = quotes.content
    soup = BeautifulSoup(quotes, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip('""')
        author = quote.find('small', class_='author').text.strip()

        # Extract all tags as a list and join them into a single string
        tag_list = [tag.text for tag in quote.find_all('a', class_='tag')]
        tags = ", ".join(tag_list)

        all_quotes.append([text, author, tags])

print(all_quotes)

df = pd.DataFrame(all_quotes, columns=['Quotes', 'Author', 'Tags'])
df.to_csv('all_quotes.csv')
