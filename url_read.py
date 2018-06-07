# Print all the headings from New York times

import requests
from bs4 import BeautifulSoup 

url = "https://www.nytimes.com/"

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

title = soup.find('div','title')
print(title)
