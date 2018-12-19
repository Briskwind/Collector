import difflib
import os
import pickle

import joblib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

django.setup()
from sklearn.neighbors import NearestNeighbors





def show_chinese( id_array, pk_list_set):
    # book = Book.objects.get(pk=pk)
    # tags = book.tag.all().values_list('tag_name', flat=1)
    # print('搜索书籍:', book.name, list(tags))

    pk_list = []
    for i in id_array:
        pk = pk_list_set[int(i)]
        pk_list.append(pk)

    print('pk_list ', pk_list)



def get_similar_book( plk_file, all_book_pk_file):
    """ 获得相似的书籍"""
    data = '0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|1|0|1|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|0|0'
    data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    target = [data]
    nbrs = joblib.load(plk_file)

    distances, indices = nbrs.kneighbors(target)
    pk_list_set = pickle.load(open(all_book_pk_file, 'rb'))


    show_chinese( indices[0], pk_list_set)


def fit_data_and_dump_plk(data_file, plk_file):
    """ 训练数据并打包模型"""

    def make_data_list():
        data_list = []
        with open(data_file, 'r') as f:
            data = f.readlines()
            for line in data:
                line_list = line.split('|')
                test_data = [int(x) for x in line_list[:-1]]
                if len(test_data) != 49:
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


    # 对数据进行训练、进行模型存储
    fit_data_and_dump_plk(data_file, plk_file)

    # 训练成功之后,从数据集提取书籍id
    make_all_book_pk_file(data_file, all_book_pk_file)


plk_file =  '/Users/xufengxu/tianzhu_pro/eyaos_web/web/xsl.plk'
data_file = '/Users/xufengxu/tianzhu_pro/eyaos_web/web/xsl.data'
all_book_pk_file = '/Users/xufengxu/tianzhu_pro/eyaos_web/web/xsl_pk.data'
# fit_data_and_dump_plk(data_file, plk_file)

# make_all_book_pk_file(data_file, all_book_pk_file)


# 获取书籍相似书籍
# book = Book.objects.get(pk=5534)
get_similar_book(plk_file, all_book_pk_file)




