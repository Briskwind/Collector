### Collector

#### 开发环境
```
python3.5
后台进程管理:pm2
```

#### web demo 小栗子

#### gunicorn 启动web
```bash

# 启动worker
celery -A celery_pro worker -l info -c 1
# 启动beat,可以在启动worker中增加-B 参数替代
celery -A celery_pro beat  -l info 

Collector/deploy/gunicorn
pm2 start web.sh
```


#### 记录笔记
```bas
增加爬取微博热搜定时任务
增加了异步任务、超时重试等
增加了日志配置
```
