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
    books = Book.objects.filter(tag__isnull=True)
    print(books.count())

    for book in books:
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

        res = requests.get(url, headers=headers, timeout=15)

        text = res.content
        soup = BeautifulSoup(text, "lxml")
        tags = soup.find_all('a', {'class': ' tag'})
        print('len tags', len(tags))
        for tag in tags:
            tag_name = tag.text
            res = BookTag.objects.filter(tag_name=tag_name).first()
            if res:
                book.tag.add(res)



def get_ip_data():
    import requests

    url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=af24def308ab4c3a920f38f937f14b96&count=1&expiryDate=0&format=1&newLine=2'
    res = requests.get(url)
    res.json()
    data = res.json()
    print('data', data)
    ip_data = '{0}:{1}'.format(data['msg'][0]['ip'], data['msg'][0]['port'])
    return ip_data

ip_data = '125.112.39.193:38096'
while True:
    try:
        print('ip_data', ip_data)
        make_tag(ip_data)
    except Exception as e:
        ip_data = get_ip_data()
        print(e)
        pass
