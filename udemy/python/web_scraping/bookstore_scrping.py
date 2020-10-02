import bs4
import requests
# toscrape.com is used for testing the  

base_url = "http://books.toscrape.com/catalogue/category/books_1/page-{}.html"

for page in range(1,2):
    url = base_url.format(page)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    product = soup.select('.product_pod')
    
    for item in product:
        star_ating_two = item.select(".star-rating.Two")
        if len(star_ating_two) == 1:
            title = item.select('a')
            image = item.select('a>img')['src']
            print(image)
            #print(title[1]['title'])
            #print(title[0]['src'])

            