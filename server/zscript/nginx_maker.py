""" 生成基本的nginx配置"""

config = {
    'sock_file': 'unix:/Users/xufengxu/git_pro/Collector/server/gunicorn.sock',
    'server_name': '127.0.0.1',
    'web_root': '/Users/xufengxu/git_pro/Collector/server/',
    'static_path': '/Users/xufengxu/git_pro/Collector/server/',
    'access_log_path': '/Users/xufengxu/git_pro/Collector/server/logs/nginx.access.log',
    'error_logpath': '/Users/xufengxu/git_pro/Collector/server/logs/nginx.error.log'
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

print('template', template)
