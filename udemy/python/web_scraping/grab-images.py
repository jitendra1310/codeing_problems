import os
import urllib.parse as urlparse
import bs4
import requests

url = ("http://example.com/",'https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam')
result = requests.get(url[1])
soup = bs4.BeautifulSoup(result.text,'lxml')
images = soup.select(".image img")

for image in images:
    img_url = "https:"+image['src']
    file_name = os.path.basename(img_url)
    img_content = requests.get(img_url)
    f = open(file_name,'wb')
    f.write(img_content.content)
    f.close()