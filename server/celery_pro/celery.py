from __future__ import absolute_import

import os
from celery import Celery
from celery import platforms

# from server import settings

from server import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

platforms.C_FORCE_ROOT = True

app = Celery('celery_pro', include=['celery_pro.tasks'])

app.config_from_object('celery_pro.celery_config')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
