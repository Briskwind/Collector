
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
