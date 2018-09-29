""" 根据项目相对路径配置相应的gunicorn 文件"""

import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

bind_file = 'unix:{0}/gunicorn.sock'.format(BASE_DIR)
chdir_path = "{0}".format(BASE_DIR)
accesslog_path = "{0}/logs/gunicorn_access.log".format(BASE_DIR)
errorlog_path = "{0}/logs/gunicorn_error.log".format(BASE_DIR)

bind = bind_file


# bind = '127.0.0.1:8001'
backlog = 512
workers = 2

worker_class = 'gevent'
chdir = chdir_path
accesslog = accesslog_path
errorlog = errorlog_path
