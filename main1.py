import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta



def fetch_news(url):
    try:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        news_items = soup.find_all('div', class_='rubric_lenta')  

        for item in news_items:
            heading = item.find('a', class_='uho__link uho__link--overlay').text.strip() 
            summary = item.find('h3', class_='uho__subtitle rubric_lenta__item_subtitle').text.strip()  
            source = item.find('a', class_='tag_list__link').text.strip() 

            
            if 'республик' in item.text or 'демократич' in item.text:
                print(f'Заголовок: {heading}')
                print(f'Аннотация: {summary}')
                print(f'Авторы: {source}')
            else:
                print('-')
    except Exception as e:
        print(f'Ошибка при извлечении новостей: {e}')



def run_script(duration_hours):
    end_time = datetime.now() + timedelta(hours=duration_hours)
    print(f'Скрипт запущен на {duration_hours} часов. Время окончания: {end_time}')

    while datetime.now() < end_time:
        
        url = 'https://www.kommersant.ru/lenta'  
        fetch_news(url)

       
        time.sleep(6)
        print('Новый запуск поиска')



run_script(4)