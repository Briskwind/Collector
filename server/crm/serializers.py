from rest_framework import serializers

from crm.models import News


class NewsSerializer(serializers.ModelSerializer):
    creation_time = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('pk', 'text', 'url', 'news_type', 'hot_count', 'images', 'platform', 'creation_time')

    def get_creation_time(self, obj):
        return obj.creation_time.strftime('%Y-%m-%d %H:%M:%S')
