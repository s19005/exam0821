import requests
from bs4 import BeautifulSoup


def check_weather(url, d):
    # 引数dで今日(today)か明日(tomorrow)の天気のどちらかを選べる
    r = requests.get(url)

    b = BeautifulSoup(r.content, 'html.parser')

    day = b.find(class_='{}-weather'.format(d))
    weather = day.p.string

    temp = day.div.find(class_='date-value-wrap')

    # 最高気温と最低気温
    temp = temp.find_all('dd')
    temp_max = temp[0].span.string
    temp_min = temp[2].span.string

    print('天気:{}'.format(weather))
    print('最高気温:{}'.format(temp_max))
    print('最低気温:{}'.format(temp_min))
    print('')
# 浦添市の天気のURL
url = 'https://tenki.jp/forecast/10/50/9110/47208'

print('今日--------------------')
check_weather(url, 'today')
print('明日--------------------')
check_weather(url, 'tomorrow')
