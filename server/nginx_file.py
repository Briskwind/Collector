""" nginx test"""
"""
    return 301 https://www.syzljh.cn$request_uri;
    rewrite ^/(.*) http://test.syzljh.com/$1 permanent;
    isten 443 default http2 fastopen=3 reuseport
    client_max_body_size
    ssl_dhparam
    ssl_ciphers
    ssl_prefer_server_ciphers
    ssl_protocols
    ssl_session_cache
    ssl_session_timeout


    ssl_session_tickets
    ssl_session_ticket_key
    resolver
    resolver_timeout
    log_not_found
    set $valid_host 0;
    try_files $uri  @proxy_to_app;
    $uri
    $query_string


    add_header       Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto http;
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_redirect off;
    proxy_ignore_client_abort on;
    proxy_pass   http://wangqian_app_server;

"""
