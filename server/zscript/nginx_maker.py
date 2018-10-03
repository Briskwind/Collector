""" 生成基本的nginx配置"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

from server.settings import BASE_DIR
from zscript.gunicorn import bind_file

django.setup()
config = {
    'sock_file': bind_file,
    'server_name': '127.0.0.1',
    'web_root': BASE_DIR,
    'static_path': os.path.join(BASE_DIR, 'static/'),
    'access_log_path': os.path.join(BASE_DIR, 'logs/nginx.access.log'),
    'error_logpath': os.path.join(BASE_DIR, 'logs/nginx.error.log')
}

template = """
upstream  web_server {{
    server {sock_file} fail_timeout=0;
    }}
server {{
    listen 80;
    server_name {server_name};
    charset utf-8;
    root {web_root};
    location @proxy_to_app {{
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://web_server;
       }}
    location ~ ^/ {{
        try_files $uri @proxy_to_app;
    }}
    location /static/ {{
        root  {static_path};
            }}
access_log {access_log_path};
error_log {error_logpath};
}}
""".format(**config)


# python sqlmap.py -u "http://127.0.0.1:9090/user/api/login/?id=1" --auth-type Basic --auth-cred "67444758@tianzhu.com:67444758"


print('template', template)
