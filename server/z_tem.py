import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

django.setup()

from crm.models import BookTag, Book

import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=960&type=T'
res = requests.get(url)

text = res.content
soup = BeautifulSoup(text, "lxml")
items = soup.find_all('li', {'class': "subject-item"})

"""

book_id = models.CharField('豆瓣id', max_length=64)
name = models.CharField('书名称', max_length=128)

"""

for item in items[:2]:

    cover = item.find('a', {'class': "nbg"}).find('img').attrs['src']
    url = item.find('a', {'class': "nbg"}).attrs['href']
    introduction = item.find('p').text.replace('\n', '')
    score = item.find('span', {'class': "rating_nums"}).text
    data = item.find('div', {'class': "pub"}).text.replace('\n', '').replace(' ', '').split('/')
    author = data[0]
    price = data[-1]
    publish = data[-3]

    name = item.find('h2').text.replace('\n', '').replace(' ', '')
    tem_data = url.split('/')
    book_id = tem_data[-2]

    print('name', name)
    print('book_id', book_id)
    print('score', score)
    print('url', url)
    print('cover', cover)
    print('introduction', introduction)
    print('author', author)
    print('price', price)
    print('publish', publish)
    print('+++++++++++++++')

"""
 <li class="subject-item">
<div class="pic">
<a class="nbg" href="https://book.douban.com/subject/25862578/" onclick="moreurl(this,{i:'0',query:'',subject_id:'25862578',from:'book_subject_search'})">
<img class="" src="https://img3.doubanio.com/view/subject/m/public/s27264181.jpg" width="90"/>
</a>
</div>
<div class="info">
<h2 class="">
<a href="https://book.douban.com/subject/25862578/" onclick="moreurl(this,{i:'0',query:'',subject_id:'25862578',from:'book_subject_search'})" title="解忧杂货店">

    解忧杂货店




  </a>
</h2>
<div class="pub">


  [日] 东野圭吾 / 李盈春 / 南海出版公司 / 2014-5 / 39.50元

      </div>
<div class="star clearfix">
<span class="allstar45"></span>
<span class="rating_nums">8.6</span>
<span class="pl">
        (325958人评价)
    </span>
</div>
<p>现代人内心流失的东西，这家杂货店能帮你找回——
僻静的街道旁有一家杂货店，只要写下烦恼投进卷帘门的投信口，第二天就会在店后的牛奶箱里得到回答。
因男友身患绝... </p>
<div class="ft">
<div class="collect-info">
</div>
<div class="cart-actions">
<span class="market-info">
<a href="https://book.douban.com/subject/25862578/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
</span>
</div>
</div>
</div>
</li>



"""
