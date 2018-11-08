# from datetime import timedelta

# from kombu import Queue
# from datetime import timedelta
from datetime import timedelta

from celery.schedules import crontab

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/3'

BROKER_URL = 'redis://127.0.0.1:6379/4'

# BROKER_URL = 'amqp://guest:guest@localhost/'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']



CELERYBEAT_SCHEDULE = {
    # 'add-every-30-seconds': {
    #     'task': 'celery_pro.tasks.fail_restart',
    #     'schedule': timedelta(seconds=60),
    #     'args': (16, 0)
    # },

    'get_weibo_top': {
        'task': 'crm.tasks.get_weibo_top_data',
        'schedule': timedelta(seconds=60),
    },


}
