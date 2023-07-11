import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Collect the links (existing code)

base_url = 'https://lobby-ethics.maryland.gov/public_access?filters%5Bar_date_end%5D=&filters%5Bar_date_start%5D=&filters%5Bar_lobbying_year%5D=&filters%5Bc_date_end%5D=&filters%5Bc_date_start%5D=&filters%5Bc_lobbying_year%5D=&filters%5Bdate_selection%5D=Lobbying+Year&filters%5Bemployer_name%5D=&filters%5Blar_date_end%5D=&filters%5Blar_date_start%5D=&filters%5Blar_lobbying_year%5D=&filters%5Blobbying_year%5D=&filters%5Breport_type%5D=Activity+Reports&filters%5Breports_containing%5D=&filters%5Bsearch_query%5D=&page='
pages = 100  # Define the number of pages you want to scrape

links = []

for page in range(1, pages + 1):
    url = base_url + str(page)

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')

    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            for link in cell.find_all('a'):
                links.append("https://lobby-ethics.maryland.gov/" + link['href'])

with open('./links.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Link'])
    writer.writerows([[link] for link in links])

# Step 2: Scrape information from each link
data = []

for link in links:
    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find('table', {'class': 'grid'}).text.strip()

    for row in info.find_all('tr'):
        for cell in row.find_all('td'):

    # Append the extracted information to the data list
    data.append([info])

# Step 3: Write the data to a CSV file
with open('./information.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Info', 'Details'])
    writer.writerows(data)


