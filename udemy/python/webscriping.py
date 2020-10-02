#!/usr/bin/python3.7
import requests
import bs4
result = requests.get("http://example.com/")
soup = bs4.BeautifulSoup(result.text,'lxml')
site_title = soup.select('title')
print(site_title[0].text)
