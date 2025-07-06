# 📚 Book Scraper – BooksToScrape.com

A simple Python project that scrapes book information (titles, prices, and star ratings) from [BooksToScrape.com](https://books.toscrape.com), a mock site made for practicing web scraping. The data is collected across all 50 catalog pages and saved in a CSV file.

---

## 🔍 Features

- ✅ Extracts **book title**, **price**, and **star rating**
- ✅ Automatically loops through **all 50 pages**
- ✅ Saves data to a clean `books.csv` file
- ✅ Beginner-friendly code with clear comments
- ✅ Built using **requests**, **BeautifulSoup**, and **pandas**

---

## 📁 Output Example

| Title                | Price | Star Rating |
| -------------------- | ----- | ----------- |
| A Light in the Attic | 51.77 | Three       |
| Tipping the Velvet   | 53.74 | One         |
| Sharp Objects        | 47.82 | Four        |

---

## 🧰 Requirements

Make sure you have Python 3 installed, then install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```
