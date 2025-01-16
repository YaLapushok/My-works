import requests
from bs4 import BeautifulSoup as bs
from time import sleep


def parser(name:str,teg:str):
    name = name.strip().replace(' ','+')
    url = f'https://www.avito.ru/ufa?cd=1&p=1&q={name}'
    r = requests.get(url)
    sleep(2)
    soup = bs(r.text,'html.parser')
    # try:
    #     last_page = soup.find('li',class_='styles-module-listItem_last-RzX6e')
    #     last_page = [int(i['data-value']) for i in last_page][0]
    # except:
    last_page = soup.find('li', class_='styles-module-item_last-iHvU3')
    print(last_page,r.status_code)
    last_page = [int(i['data-value']) for i in last_page][0]
    for i in range(1,last_page+1):
        sleep(5)
        '''90 элемент url это номер страницы, мы её меняем'''
        if i<=10:
            url = url.replace(url[32],str(i))
        else:
            url = url.replace(url[34:36],str(i))
        sleep(5)
        r = requests.get(url=url)
        sleep(5)
        soup = bs(r.text,'html.parser')
        data_marker = soup.find_all('div',{'data-marker':'item'})
        for marker in data_marker:
            '''data-marker - список объявлений'''
            meta = marker.find('meta')
            content = meta['content']
            url_page = marker.find('div', class_='styles-module-theme-rOnN1')
            url_page ='avito.ru'+url_page.find('a',class_='iva-item-sliderLink-uLz1v')['href']
            if str(teg) in content:
                return content,url_page