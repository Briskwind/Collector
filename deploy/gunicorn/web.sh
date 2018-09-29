
PWD=$('pwd')
ADD='/../../server'
PROJECT_PATH=${PWD}${ADD}
CONFROOT=./zscript/gunicorn.py

cd $PROJECT_PATH
exec /Users/xufengxu/.pyenv/versions/shouy/bin/gunicorn server.wsgi:application -c $CONFROOT
