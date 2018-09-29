bind = 'unix:/Users/xufengxu/git_pro/Collector/server/gunicorn.sock '

# bind = '127.0.0.1:8001'
backlog = 512
workers = 2

worker_class = 'gevent'
chdir = '/Users/xufengxu/git_pro/Collector/server'
accesslog = "/Users/xufengxu/git_pro/Collector/server/logs/gunicorn_access.log"
errorlog = "/Users/xufengxu/git_pro/Collector/server/logs/gunicorn_error.log"