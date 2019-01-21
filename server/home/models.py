from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.db import models


# Create your models here.


class User(models.Model):
    """ 用户模型"""

    account = models.CharField('账号', max_length=64)
    password = models.CharField('密码', max_length=80)
    name = models.URLField('姓名', null=True, blank=True, default='')
    creation_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)


class Stock(models.Model):
    """ Stock"""
    open = models.CharField('开盘', max_length=500)
    high = models.CharField('最高', max_length=500)
    low = models.CharField('最低', max_length=500)
    close = models.CharField('收盘', max_length=500)
    chg = models.CharField('涨跌额度', max_length=500)
    percent = models.CharField('涨跌幅', max_length=500)
    turnoverrate = models.CharField('换手率', max_length=500)
    volume = models.CharField('成交额', max_length=500)
    close_minus_open = models.CharField('收盘减去开盘', max_length=500)
    high_start = models.BooleanField('是否是高开', default=False)
    stock_name = models.CharField('股票名称', max_length=500, null=True, blank=True, default='上证')
    yesterday_close = models.CharField('昨日收盘', max_length=500, null=True, blank=True, default='')
    date_time = models.DateTimeField(null=True, blank=True, default=None)
    timestamp = models.CharField('时间', max_length=500)

    def __str__(self):
        return self.stock_name

    class Meta:
        db_table = 'Stock'
        verbose_name = verbose_name_plural = '股票'
