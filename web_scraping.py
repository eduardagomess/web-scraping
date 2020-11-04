from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.rubyrosemaquiagem.com.br/rosto?PS=48&O=OrderByReleaseDateDESC')
soup = BeautifulSoup(res.text, 'html.parser')
all_products = soup.find_all(class_ = 'body-shelf')
all_prices = soup.find_all(class_ = 'best-price')

products = []
prices = []

[products.append((product.find('strong').text)) for product in all_products]

[prices.append((price.text)) for price in all_prices]

catalogo = dict(zip(products, prices))

