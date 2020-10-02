import requests
import bs4 

url = ("http://example.com/",'https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam')
result = requests.get(url[1])
soup = bs4.BeautifulSoup(result.text,'lxml')
site_title = soup.select('title')[0].getText()
site_paragraph = soup.select('p')
site_paragraph_item_list = set()
for site_paragraph_item in site_paragraph:  
    site_paragraph_item_list.add(site_paragraph_item.getText())
    
    
print(site_paragraph_item_list)