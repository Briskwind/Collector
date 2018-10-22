from celery_pro.celery import app
from extensions.weibo_top import get_weibo_top


@app.task(ignore_result=True)
def get_weibo_top_data():
    """定时获取微博热搜排行榜"""
    get_weibo_top()

