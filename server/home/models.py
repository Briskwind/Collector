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
