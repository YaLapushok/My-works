import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2Fproduct%2Fredmi-smartfon-note-11-pro-8-256-gb-chernyy-1513551804%2F%3Fadvert%3DcbCEoLvcKV0p68-V7lt6O4d_tlA4CvgIi6ZHzrfemghGkuMn37KyX1nZWoVYGbdeeJH03smTYCJH-5mtwxC_1hpc5RYsEtCXbj_SdhRIYC6nq8aNcMg-Tm5mco40THMK9ussdns80EFkPXVC1Ok4if2u0N_UH3Q9I4GhYbo79FoZS8pVwO8x_6WpXLt6qxidud7Wh8WqS1JjYtNoWuEaAVDQZCMsOZYiI-lzJTh6oxTNb9fn4Li5AQpvFkYaY2GkfbARAec%26avtc%3D1%26avte%3D2%26avts%3D1712734371%26layout_container%3DpdpPage2column%26layout_page_index%3D2%26sh%3DsNWe9XYF6Q%26start_page_id%3Dbd775cf09a79c92ff140aef73fe53aec'
    response = requests.get(url=url)
    print(response.json())
if __name__=='__main__':
    main()
    