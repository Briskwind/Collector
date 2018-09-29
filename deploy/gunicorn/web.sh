
PROJECT_PATH=/Users/xufengxu/git_pro/Collector/server
CONFROOT=./gunicorn.py

cd $PROJECT_PATH
exec /Users/xufengxu/.pyenv/versions/shouy/bin/gunicorn server.wsgi:application -c $CONFROOT
