import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

def get_tablets_row_path(soup):
    
    tablets_cards = soup.select('body > div.wrapper > div.container.test-site > div.row > div.col-lg-9 > div.row > div.col-md-4.col-xl-4.col-lg-4')
    return tablets_cards

def get_price(div):
    
    price = div.find('span', attrs = {'itemprop' : 'price'}).text.strip()
    price = price.replace("$", "")
    price = float(price)
    return price

def get_link(div):
    
    link = div.find('a', class_='title')
    return link['href']

def get_name(div):
    
    name = div.find('a', class_= 'title').text.strip()
    return name

def get_description(div):
    
    description = div.find('p', class_= 'description card-text').text.strip()
    return description

def get_product(div):
    
    price = get_price(div)
    link = get_link(div)
    name = get_name(div)
    description = get_description(div)
    product = {"name" : name, "description" : description, "price": price, "link": link}
    return product
    
    
listOfTablets = get_tablets_row_path(soup)


tablet = get_product(listOfTablets[0])


    







