import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news")
html_code = response.text

soup = BeautifulSoup(html_code, "html.parser")

h2_tags = soup.find_all('h2')

for tag in h2_tags:
    print(tag.text)

programs = soup.find_all('h2', {"class": "wp-block-heading"})
for progr in programs:
    print(progr.text)