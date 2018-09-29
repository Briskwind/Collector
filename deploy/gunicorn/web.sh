
PWD=$('pwd')
ADD='/../../server'
PROJECT_PATH=${PWD}${ADD}
CONFROOT=./zscript/gunicorn.py

cd $PROJECT_PATH
exec /root/.pyenv/versions/web/bin/gunicorn server.wsgi:application -c $CONFROOT
