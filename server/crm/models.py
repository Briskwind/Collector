from datetime import datetime
from django.db import models


# Create your models here.




class News(models.Model):
    """ 新闻模型"""

    text = models.CharField('标题', max_length=64)
    url = models.CharField('链接', max_length=256)
    news_type = models.CharField('新闻类型', max_length=64)
    images = models.CharField('图片', max_length=512, default='')
    platform = models.URLField('平台', null=True, blank=True, default='')
    creation_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '新闻资讯'
        verbose_name_plural = '新闻资讯'
