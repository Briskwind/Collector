""" 获取微博top20热搜"""
from bs4 import BeautifulSoup

from crm.models import News
import requests


def get_weibo_top():
    """ 获取微博热搜"""

    url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
    base_url = 'https://s.weibo.com'
    res = requests.get(url)
    text = res.content
    soup = BeautifulSoup(text, "lxml")
    items = soup.find_all('a', {'target': '_blank'})
    data = []
    all_news = News.objects.all().values_list('text', flat=True)

    news_list = []
    for item in items:
        data_item = {}
        url = item.attrs['href']
        text = item.text

        if url.endswith('top') and text not in all_news:
            data_item['text'] = text
            data_item['url'] = base_url + url
            data_item['platform'] = 'sina'
            data.append(data_item)
            news_list.append(News(**data_item))

    News.objects.bulk_create(news_list)
    return news_list
