import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

class BaseParser():
    def __init__(self):
        self.URL = "https://qalampir.uz/uz/news/category/olam"

    def get_soup(self):
        try:
            res = requests.get(self.URL).text
            soup = BeautifulSoup(res, 'html.parser')
            return soup

        except:
            print("Noto'g'ri ma'lumot kiritildi")


class CategoryParser(BaseParser):
    def __init__(self):
        super().__init__()

        try:
            soup = self.get_soup()
            box = soup.find('div', class_='row g-4')
            products = box.find_all('div', class_='col-lg-4 col-md-6')[:10]
            news_list = []
            for item in products:
                title = item.find('p',class_='news-card-content-text').text
                source = item.find('a', class_='news-card')['href']
                link = 'https://qalampir.uz/' + source
                visibility = item.find('span',class_='type-text').text
                date = item.find('span', class_='date').text
                news_list.append({'title': title,'link': link ,'visibility': visibility,'date': date})
            with open('data.json', mode='w',encoding='utf-8') as file:
                json.dump(news_list, file, ensure_ascii=False, indent=4)
        except:
            print('sdfsfs')


CategoryParser()
























