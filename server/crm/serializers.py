from rest_framework import serializers

from crm.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('pk', 'text', 'url', 'news_type', 'hot_count','images','platform','creation_time')
