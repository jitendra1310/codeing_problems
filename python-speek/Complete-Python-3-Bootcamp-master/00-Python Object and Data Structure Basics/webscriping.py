import requests
import bs4


result = requests.get("http://example.com/")
bs4.BeautifulSoup(result.content,'lxml')