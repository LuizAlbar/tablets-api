import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")


divs = soup.select("div.col-md-4.col-xl-4.col-lg-4")

firstDiv = divs[0]

def get_price(div):
    
    price = div.find('span', attrs = {'itemprop' : 'price'}).text.strip()
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

def get_id(div):
    
    link = div.find('a', class_='title')
    link = link['href']
    id = link.split('/')
    id = id[-1]
    return id

def make_product(div):
    
    price = get_price(div)
    link = get_link(div)
    name = get_name(div)
    description = get_description(div)
    id = get_id(div)
    product = (price, link, name, description, id)
    
    return product
    

for div in divs:
    produto = make_product(div)


    
    







