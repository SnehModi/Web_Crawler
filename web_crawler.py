import requests
from bs4 import BeautifulSoup
import pandas as pd


def next_link(link_url):
    pages = requests.get(link_url)
    soups = BeautifulSoup(pages.content, "html.parser")
    fetch = [soups.find(class_='Pcpdetail2').get_text()]
    # print(fetch)
    return fetch


page = requests.get("https://wap.stonecontact.com/suppliers/stone-importer/united-states-country")
soup = BeautifulSoup(page.content, "html.parser")
# x = soup.find_all('div')
y = soup.find_all(class_='SIndexText')
z = soup.find_all('a', attrs={'class': 'sindexsupplier'})
# print(y[0])

# print(y[0].find(class_='sindexsupplier').get_text())
# print(y[0].find(class_='sindexCountry').get_text())

Company = []
Address = []
b_type = []
for x in y:
    Company.append(x.find(class_='sindexsupplier').get_text())
    Address.append(x.find(class_='sindexCountry').get_text())
for link in z:
    # link.find('a', attrs={'class': 'sindexsupplier'})
    href = link.get('href')
    url = "https://wap.stonecontact.com" + href
    temp = next_link(url)
    b_type.append(temp)
    # print(href)

print(Company)
print(Address)
print(b_type)

scraped_data = pd.DataFrame(
    {
        'Company': Company,
        'Address': Address,
        'Details': b_type,
    })

scraped_data.to_csv('Web_Crawl_details.csv')
