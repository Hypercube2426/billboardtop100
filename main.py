from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
bill_board = response.text
soup = BeautifulSoup(bill_board, 'html.parser')
print(soup.prettify())
