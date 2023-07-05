import requests
from bs4 import BeautifulSoup

url = 'https://lobby-ethics.maryland.gov/public_access?filters%5Bar_date_end%5D=&filters%5Bar_date_start%5D=&filters%5Bar_lobbying_year%5D=&filters%5Bc_date_end%5D=&filters%5Bc_date_start%5D=&filters%5Bc_lobbying_year%5D=&filters%5Bdate_selection%5D=Lobbying+Year&filters%5Bemployer_name%5D=&filters%5Blar_date_end%5D=&filters%5Blar_date_start%5D=&filters%5Blar_lobbying_year%5D=&filters%5Blobbying_year%5D=&filters%5Breport_type%5D=Activity+Reports&filters%5Breports_containing%5D=&filters%5Bsearch_query%5D=&page=2'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
a_href=soup.find("a",{"class":" btn-link blue"}).get("href")
print(table.prettify())

