import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
def fetch_news(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('div', class_='rubric_lenta')  #
        for item in news_items:
            if 'республик' in item.text or 'демократич' in item.text:
                print(f'Новость: {heading}')
                print(f'Содержание: {argument}')
                print(f'Источник: {source}')
            else:
                print('-')
            heading = item.find('span', class_='vam').text.strip()
            argument = item.find(
                'h3',
                class_='uho__subtitle rubric_lenta__item_subtitle').text.strip(
                )
            source = item.find('a', class_='tag_list__link').text.strip()
    except Exception as e:
        print(f'сбой: {e}')


def run_script(duration_hours):
    end_time = datetime.now() + timedelta(hours=duration_hours)
    print(
        f'Время работы программы {duration_hours} часа. Закончит работу: {end_time}'
    )

    while datetime.now() < end_time:
        url = 'https://www.kommersant.ru/lenta?ysclid=lwxx2s7elm606723236'
        fetch_news(url)


run_script(4)
