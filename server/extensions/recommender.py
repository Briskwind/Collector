import pickle

import joblib

from crm.models import Book
from server.settings import ALL_BOOK_PK_FILE, PLK_FILE

TAGS = ['三毛', '东野圭吾', '个人管理', '中国', '中国历史', '中国文学', '互联网', '亦舒', '人性', '人文', '人物传记', '人生', '人类学', '传记', '余华', '儿童文学',
        '励志', '历史', '古典文学', '台湾', '名著', '哲学', '商业', '回忆录', '国学', '外国文学', '奇幻', '女性', '好书，值得一读', '安妮宝贝', '宗教', '小说',
        '工具书', '建筑', '张爱玲', '当代文学', '德国', '心灵', '心理', '心理学', '思想', '思维', '悬疑', '成长', '我想读这本书', '投资', '推理', '推理小说', '摄影',
        '政治', '政治哲学', '政治学', '教材', '教育', '散文', '散文随笔', '数学', '文化', '文学', '旅行', '日本', '日本文学', '日本漫画', '日系推理', '时间管理',
        '杂文', '村上春树', '東野圭吾', '武侠', '毛姆', '治愈', '法国', '法国文学', '温暖', '游记', '漫画', '爱情', '王小波', '生活', '电影', '社会', '社会学',
        '科学', '科幻', '科幻小说', '科普', '穿越', '童话', '管理', '纪实', '经典', '经济', '经济学', '绘本', '编程', '网络小说', '美国', '美国文学', '美食',
        '耽美', '职场', '艺术', '英国', '英国文学', '英文原版', '英语', '营销', '言情', '计算机', '设计', '诗歌', '轻小说', '郭敬明', '金庸', '金融',
        '阿加莎·克里斯蒂', '随笔', '青春', '韩寒', '香港']


def show_chinese(pk, id_array, pk_list_set):
    book = Book.objects.get(pk=pk)
    tags = book.tag.all().values_list('tag_name', flat=1)
    print('搜索书籍:', book.name, list(tags))

    pk_list = []
    for i in id_array:
        pk = pk_list_set[int(i)]
        pk_list.append(pk)

    print(' ')
    books = Book.objects.filter(pk__in=pk_list)

    name_list = []
    for book in books:
        tag = book.tag.all().values_list('tag_name', flat=1)
        print('相似书籍', book.name, book.score, '   ', ' '.join(list(tag)))
        name_list.append(book.name)

    print('name_list', name_list)


def make_one_data(book):
    """ 生产一条记录"""

    tags_list = ['0' for i in range(0, 120)]
    tags_names = list(book.tag.all().values_list('tag_name', flat=1))

    for i in tags_names:
        index = TAGS.index(i)
        tags_list[index] = '1'

    assert len(tags_list) == 120
    return tags_list


class BookRecommender():
    """ 书籍推荐者"""
    NBRS = joblib.load(PLK_FILE)
    PK_LIST_SET = pickle.load(open(ALL_BOOK_PK_FILE, 'rb'))

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return cls._instance
        cls._instance = super(BookRecommender, cls).__new__(cls, *args)
        return cls._instance

    def recommender(self, book):
        target_book_data = make_one_data(book)
        distances, indices = BookRecommender.NBRS.kneighbors([target_book_data])

        show_chinese(book.pk, indices[0], BookRecommender.PK_LIST_SET)
