from rest_framework import serializers

from crm.models import News, Book


class NewsSerializer(serializers.ModelSerializer):
    creation_time = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('pk', 'text', 'url', 'news_type', 'hot_count', 'images', 'platform', 'creation_time')

    def get_creation_time(self, obj):
        return obj.creation_time.strftime('%Y-%m-%d %H:%M:%S')


class BookSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('pk', 'name', 'author', 'price', 'publish', 'url', 'cover', 'create_time')

    def get_url(self, obj):
        return obj.url.strip()

    def get_name(self, obj):
        return obj.name.strip()

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
