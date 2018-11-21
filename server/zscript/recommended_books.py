import difflib
import os
import pickle

import joblib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

django.setup()
from sklearn.neighbors import NearestNeighbors

from crm.models import BookTag, Book

tags = ['三毛', '东野圭吾', '个人管理', '中国', '中国历史', '中国文学', '互联网', '亦舒', '人性', '人文', '人物传记', '人生', '人类学', '传记', '余华', '儿童文学',
        '励志', '历史', '古典文学', '台湾', '名著', '哲学', '商业', '回忆录', '国学', '外国文学', '奇幻', '女性', '好书，值得一读', '安妮宝贝', '宗教', '小说',
        '工具书', '建筑', '张爱玲', '当代文学', '德国', '心灵', '心理', '心理学', '思想', '思维', '悬疑', '成长', '我想读这本书', '投资', '推理', '推理小说', '摄影',
        '政治', '政治哲学', '政治学', '教材', '教育', '散文', '散文随笔', '数学', '文化', '文学', '旅行', '日本', '日本文学', '日本漫画', '日系推理', '时间管理',
        '杂文', '村上春树', '東野圭吾', '武侠', '毛姆', '治愈', '法国', '法国文学', '温暖', '游记', '漫画', '爱情', '王小波', '生活', '电影', '社会', '社会学',
        '科学', '科幻', '科幻小说', '科普', '穿越', '童话', '管理', '纪实', '经典', '经济', '经济学', '绘本', '编程', '网络小说', '美国', '美国文学', '美食',
        '耽美', '职场', '艺术', '英国', '英国文学', '英文原版', '英语', '营销', '言情', '计算机', '设计', '诗歌', '轻小说', '郭敬明', '金庸', '金融',
        '阿加莎·克里斯蒂', '随笔', '青春', '韩寒', '香港']




def make_one_data(book, data_file, ret_flag=False):
    """ 生产一条记录"""

    tags_list = ['0' for i in range(0, 120)]
    pk = book.pk
    name = book.name.strip().replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '').replace('|', '-')
    tags_names = list(book.tag.all().values_list('tag_name', flat=1))

    for i in tags_names:
        index = tags.index(i)
        tags_list[index] = '1'

    assert len(tags_list) == 120

    if ret_flag:
        return tags_list

    tags_list.append(name)
    tags_list.append(str(pk))

    tag_str = '|'.join(tags_list)

    with open(data_file, 'a') as f:
        tem_data = '{0}{1}'.format(tag_str, '\n')
        f.writelines(tem_data)


def make_data(data_file):
    """ 产生样本数据"""
    books = Book.objects.all()
    for book in books:
        make_one_data(book, data_file)


def get_similar_by_name(pk_list, target_name):
    """ 匹配名字相似度"""

    print('pk_list', len(pk_list))
    similar_pk_list = []

    books_name_list = Book.objects.filter(pk__in=pk_list).values('name', 'pk')
    for item in books_name_list:
        matcher = difflib.SequenceMatcher(None, item['name'], target_name)
        if matcher.ratio() > 0.2:
            similar_pk_list.append(item['pk'])

    print('similar_pk_list', len(similar_pk_list), len(set(pk_list)&set(similar_pk_list)))

    # return sorted_pk_list


def show_chinese(pk, id_array, pk_list_set):
    book = Book.objects.get(pk=pk)
    tags = book.tag.all().values_list('tag_name', flat=1)
    print('搜索书籍:', book.name, list(tags))

    pk_list = []
    for i in id_array:
        pk = pk_list_set[int(i)]
        pk_list.append(pk)

    print(' ')
    books = Book.objects.filter(pk__in=pk_list).order_by('-score')

    get_similar_by_name(pk_list, book.name)

    name_list = []
    for book in books:
        tag = book.tag.all().values_list('tag_name', flat=1)
        print('相似书籍', book.name, book.score, '   ', ' '.join(list(tag)))
        name_list.append(book.name)

    print('name_list', name_list)


def get_similar_book(book, data_file, plk_file, all_book_pk_file):
    """ 获得相似的书籍"""
    data = make_one_data(book, data_file, ret_flag=True)

    target = [data]
    nbrs = joblib.load(plk_file)

    distances, indices = nbrs.kneighbors(target)
    pk_list_set = pickle.load(open(all_book_pk_file, 'rb'))

    show_chinese(book.pk, indices[0], pk_list_set)


def fit_data_and_dump_plk(data_file, plk_file):
    """ 训练数据并打包模型"""

    def make_data_list():
        data_list = []
        with open(data_file, 'r') as f:
            data = f.readlines()
            for line in data:
                line_list = line.split('|')
                test_data = [int(x) for x in line_list[:-2]]
                if len(test_data) != 120:
                    print(line_list[-2:-1])
                data_list.append(test_data)

        return data_list

    data_list = make_data_list()
    nbrs = NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(data_list)
    joblib.dump(nbrs, plk_file)


def make_all_book_pk_file(data_file, all_book_pk_file):
    """ 提取数据集合的pk,用作index-id 匹配"""
    data_list = []
    with open(data_file, 'r') as f:
        data = f.readlines()
        for line in data:
            line_list = line.split('|')
            data = line_list[-1]
            data_list.append(data.strip())

            if len(data.strip()) > 6:
                print(data.strip())

    list_file = open(all_book_pk_file, 'wb')
    pickle.dump(data_list, list_file)
    list_file.close()


def main(data_file, plk_file, all_book_pk_file):
    """ 整理数据、训练存储模型，提取数据"""

    # 将数据库中的数据生成训练数据集
    make_data(data_file)

    # 对数据进行训练、进行模型存储
    fit_data_and_dump_plk(data_file, plk_file)

    # 训练成功之后,从数据集提取书籍id
    make_all_book_pk_file(data_file, all_book_pk_file)


plk_file = '/Users/xufengxu/git_pro/Collector/server/book.plk'
data_file = '/Users/xufengxu/git_pro/Collector/server/book_data.data'
all_book_pk_file = '/Users/xufengxu/git_pro/Collector/server/pk_list.data'

# 获取书籍相似书籍
book = Book.objects.get(pk=5534)
get_similar_book(book, data_file, plk_file, all_book_pk_file)
