from datetime import datetime
from django.db import models


# Create your models here.

class News(models.Model):
    """ 新闻模型"""

    text = models.CharField('标题', max_length=64)
    url = models.CharField('链接', max_length=256)
    news_type = models.CharField('新闻类型', max_length=64)
    hot_count = models.IntegerField('新闻热度', blank=True, null=True)
    images = models.CharField('图片', max_length=512, default='')
    platform = models.URLField('平台', null=True, blank=True, default='')
    creation_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '新闻资讯'
        verbose_name_plural = '新闻资讯'


class BookTag(models.Model):
    """ 图书标签"""

    tag_name = models.CharField('标签', max_length=64)
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '图书标签'
        verbose_name_plural = '图书标签'


class Book(models.Model):
    """ 图书名称"""
    book_id = models.CharField('豆瓣id', max_length=64)
    name = models.CharField('书名称', max_length=128)
    author = models.CharField('作者', max_length=256)
    price = models.CharField('价格', max_length=128)
    publish = models.CharField('出版社', max_length=256)
    score = models.IntegerField('评分', default=0)
    cover = models.CharField('封面', max_length=256)
    url = models.CharField('链接', max_length=256)
    introduction = models.CharField('简介', max_length=512)
    tag = models.ManyToManyField(BookTag,verbose_name="标签",related_name="books")
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'




