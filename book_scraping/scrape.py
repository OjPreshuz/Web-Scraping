# Import the BeautifulSoup class from the bs4 module to parse HTML content
from bs4 import BeautifulSoup

# Import the requests library to make HTTP requests
import requests

# Import the pandas library to store and export data in tabular form
import pandas as pd

# Create an empty list to store book data
books = []

# Loop through page numbers 1 to 50 (there are 50 pages on the site)
for i in range(1, 51):
    # Define the URL for each page using an f-string and current page number
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    # Send an HTTP GET request to the URL and get the response
    response = requests.get(url)

    # Get the raw HTML content from the response (as bytes)
    response = response.content

    # Parse the HTML content with BeautifulSoup using the built-in HTML parser
    soup = BeautifulSoup(response, 'html.parser')

    # Optional: print the full parsed HTML (commented out)
    # print(soup.prettify())

    # Find the <ol> tag that contains all book entries
    ol = soup.find('ol')

    # Find all <article> tags with class 'product_pod' (each is a book)
    articles = ol.find_all('article', class_='product_pod')

    # Loop through each book article on the page
    for article in articles:
        # Find the <img> tag (which contains the title as alt text)
        image = article.find('img')

        # Extract the 'alt' attribute, which holds the book's title
        title = image.attrs['alt']

        # Find the <p> tag representing the star rating
        star = article.find('p')

        # Get the second class (e.g., ['star-rating', 'Three']) which is the rating
        star = star['class'][1]

        # Find the price tag <p class='price_color'> and extract text
        price = article.find('p', class_='price_color').text

        # Remove the '£' symbol and convert price to float
        price = float(price[1:])

        # Append the book's data as a list to the books list
        books.append([title, price, star])

# Print the complete list of books (each entry is [title, price, star])
print(books)

# Create a pandas DataFrame from the books list with column headers
df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])

# Export the DataFrame to a CSV file named 'books.csv'
df.to_csv('books.csv')
