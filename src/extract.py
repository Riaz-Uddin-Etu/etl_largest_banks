from bs4 import BeautifulSoup
import pandas as pd
import requests

# function to extract the tabular information from the given URL
def extract(url):
    web_page = requests.get(url)
    html_page = web_page.text
    page = BeautifulSoup(html_page, 'html.parser')
    table = page.find('table', class_="wikitable sortable mw-collapsible")
    rows = table.find_all('tr')
    data_list = list()
    for row in rows[1:]:
        col = row.find_all('td')
        if len(col) > 2:
            bank_name = col[1].get_text(strip=True)
            MC = float(col[2].get_text(strip=True))
            data_dict = {'Name': bank_name,
                         'MC_USD_Billion': MC }
            data_list.append(data_dict)
    
    dataframe1 = pd.DataFrame(data_list)
    return dataframe1

