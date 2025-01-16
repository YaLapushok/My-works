import requests
from bs4 import BeautifulSoup as bs

#url = 'https://www.avito.ru/ufa/nastolnye_kompyutery/sistemnye_bloki-ASgBAgICAUS02xKMqY0D?cd=1&p=1&q=%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80'
url = 'https://www.avito.ru/ufa?cd=1&p=2&q=системный+блок'
r = requests.get(url=url)
soup = bs(r.text,'html.parser')

last_page = soup.find('li',class_='styles-module-listItem_last-RzX6e')
last_page = [int(i['data-value']) for i in last_page]
print(last_page[0])
# data_marker = soup.find('div',{'data-marker':'item'})
# meta = data_marker.find('meta')
# #print(meta['content'])
# url_page = data_marker.find('div',class_='styles-module-theme-rOnN1')
# url_page='avito.ru'+url_page.find('a',class_='iva-item-sliderLink-uLz1v')['href']
# print(url_page)