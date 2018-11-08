
PWD=$('pwd')
ADD='/../../server'
PROJECT_PATH=${PWD}${ADD}

cd $PROJECT_PATH
exec /root/.pyenv/versions/web/bin/celery -A celery_pro worker -B -l info -c 1
