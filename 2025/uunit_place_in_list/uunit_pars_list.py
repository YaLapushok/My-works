import requests
from bs4 import BeautifulSoup as bs
import urllib3
from time import sleep
from spisok import sp

urllib3.disable_warnings()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}


def parser(snils:str,kod:str):
       sleep(6)
       r = requests.get(url=sp[kod], timeout=None,verify=False)
       soup = bs(r.text,'html.parser')
       b_mesta = soup.find('ul',class_='list-head').find_all('li')
       b_mesta= [i for i in b_mesta][7].find('span').text #Кол-во бюджетных мест .text[15:17]
       # orig = soup.find_all('tr')
       # orig = [i[9] for i in orig]
       #print(orig[0],orig[4],orig[5])
       after_snils = soup.find_all('tr',id=snils) #Находит строку с данными снилса
       for after in after_snils:
              ball = after.find_all('td') #Список из всего что есть в строке пользователя
              ball = [i for i in ball][0].text #Сделать чтобы обновлялось раз в 20 минут
              return kod,ball,b_mesta
