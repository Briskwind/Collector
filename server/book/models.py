from django.db import models
from datetime import datetime
from uuid import uuid4


# Create your models here.


class Tag():
    """ 书的标签"""
    name = models.CharField('名称', max_length=64, null=True, default='')
    creation_time = models.DateTimeField('创建时间', default=datetime.now)



class Publisher():
    """ 出版社"""
    name = models.CharField('名称', max_length=64, null=True, default='')



class Author():
    """ 作者"""
    name = models.CharField('名称', max_length=64, null=True, default='')



class Book(models.Model):
    """ 书本"""

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField('书名', max_length=500)
    price = models.DecimalField()

    publisher_time = models.CharField('出版时间', max_length=64, null=True, default='')
    creation_time = models.DateTimeField('创建时间', default=datetime.now)
