
def get_base_info(url):
    """ 获取书本的基本信息"""
    agent = generate_user_agent()

    headers = {
        'user-agent': agent,

    }
    ip_port = ip_data
    proxies = {
        'http': 'http://' + ip_port,
        'https': 'https://' + ip_port,
    }
    res = requests.get(url, proxies=proxies, headers=headers)

    text = res.content
    soup = BeautifulSoup(text, "lxml")
    items = soup.find_all('li', {'class': "subject-item"})

    book_names = Book.objects.all().values_list('name', flat=1)
    bool_list = []
    print('len items', len(items))
    for item in items:

        cover = item.find('a', {'class': "nbg"}).find('img').attrs['src']
        url = item.find('a', {'class': "nbg"}).attrs['href']
        introduction = item.find('p')
        if introduction:
            introduction = item.find('p').text.replace('\n', '')
        else:
            introduction = ''

        score = item.find('span', {'class': "rating_nums"})

        if score:
            score = item.find('span', {'class': "rating_nums"}).text
        else:
            score = 0

        try:
            score = float(score)
        except Exception as e:
            score = 0

        data = item.find('div', {'class': "pub"}).text.replace('\n', '').replace(' ', '').split('/')
        if len(data) > 3:
            author = data[0]
            price = data[-1]
            publish = data[-3]
        else:
            author = data[0]
            price = 1
            publish = ''

        name = item.find('h2').text.replace('\n', '').replace(' ', '')
        tem_data = url.split('/')
        book_id = tem_data[-2]

        data = {}
        data['name'] = name
        data['book_id'] = book_id
        data['score'] = float(score)
        data['url'] = url
        data['cover'] = cover
        data['introduction'] = introduction
        data['author'] = author
        data['price'] = price
        data['price'] = price
        data['publish'] = publish

        if name not in book_names:
            bool_list.append(Book(**data))
    print('len bool_list', len(bool_list))
    Book.objects.bulk_create(bool_list)
    return len(items)


def main():
    """ 获取书本基本信息"""
    tags = BookTag.objects.filter(check='0')
    for tag in tags:
        tag_name = tag.tag_name
        print('tag_name', tag_name)
        flag = 0
        for i in range(0, 100):
            flag = i
            url = 'https://book.douban.com/tag/{0}?start={1}&type=T'.format(tag_name, i * 20)
            print(url)

            count = get_base_info(url)
            if count == 0:
                break
        print('flag', flag)
        if flag > 40:
            tag.check = '1'
            tag.save()



import os
import sys

from requests import ConnectTimeout
from user_agent import generate_user_agent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

django.setup()

from crm.models import BookTag, Book

import requests
# from server.local_settings import ip_data

from bs4 import BeautifulSoup


def make_tag(ip_data):
    "获取详细信息，对书本进行打标签"
    books = Book.objects.filter(tag__isnull=True,  score__gt=6)[:200]
    print(books.count())

    for book in books:
        print(Book.objects.filter(tag__isnull=True, score__gt=6).count())
        url = book.url

        agent = generate_user_agent()

        headers = {
            'user-agent': agent,

        }
        ip_port = ip_data
        proxies = {
            'http': 'http://' + ip_port,
            'https': 'https://' + ip_port,
        }

        res = requests.get(url, proxies=proxies, headers=headers, timeout=15)

        text = res.content
        soup = BeautifulSoup(text, "lxml")
        tags = soup.find_all('a', {'class': ' tag'})
        print('len tags', len(tags), url)
        if len(tags) == 0:
            raise Exception('tag_is_0')
        for tag in tags:
            tag_name = tag.text
            res = BookTag.objects.filter(tag_name=tag_name).first()
            if res:
                book.tag.add(res)


def get_ip_data():
    import requests
    from server.local_settings import ip_url
    url = ip_url
    res = requests.get(url)
    res.json()
    data = res.json()
    ip_data = '{0}:{1}'.format(data['data'][0]['ip'], data['data'][0]['port'])
    print('调用接口')
    return ip_data


ip_data = '124.167.58.47:4208'
while True:
    try:
        print('ip_data', ip_data)
        make_tag(ip_data)
    except Exception as e:
        if str(e) == 'tag_is_0' or 'HTTPSConnectionPool' in str(e):
            ip_data = get_ip_data()
        continue


