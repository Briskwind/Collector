"""正式编译安装nginx"""


"""
正式药监单nginx 1.14.1 安装

cd /root/nginx1.14.1/nginx-1.14.1

./configure --user=root --group=root --prefix=/usr/local/nginx   --lock-path=/var/lock/nginx.lock --http-client-body-temp-path=/var/tmp/nginx/client --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fcgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --with-http_v2_module --with-http_ssl_module --with-stream --with-openssl=../openssl-1.1.0g --with-pcre=../pcre-8.38 --with-pcre-jit --with-zlib=../zlib-1.2.11 --with-http_realip_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_geoip_module


nginx path prefix: "/usr/local/nginx"
nginx binary file: "/usr/local/nginx/sbin/nginx"
nginx modules path: "/usr/local/nginx/modules"
nginx configuration prefix: "/usr/local/nginx/conf"
nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
nginx pid file: "/usr/local/nginx/logs/nginx.pid"
nginx error log file: "/usr/local/nginx/logs/error.log"
nginx http access log file: "/usr/local/nginx/logs/access.log"
nginx http client request body temporary files: "/var/tmp/nginx/client"
nginx http proxy temporary files: "/var/tmp/nginx/proxy"
nginx http fastcgi temporary files: "/var/tmp/nginx/fcgi"
nginx http uwsgi temporary files: "/var/tmp/nginx/uwsgi"
nginx http scgi temporary files: "scgi_temp"


/usr/local/nginx/sbin/nginx -V
/usr/local/nginx/sbin/nginx -t -c /etc/nginx/nginx.conf


原本nginx:/usr/sbin/nginx
现在nginx:/usr/local/nginx/sbin/nginx

"""





"""
正式 wq nginx 1.14.1 编译安装

# 使用lua-nginx-module-0.10.7 会有语法报错,跟新最新版本
git clone https://github.com/openresty/lua-nginx-module.git

# openssl 打补丁
mv openssl-OpenSSL_1_0_2k/ openssl
cd openssl
patch -p1 < ../sslconfig/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102j.patch



cd /data/download/nginx1.14.1



export LUAJIT_LIB=/usr/local/lib
export LUAJIT_INC=/usr/local/include/luajit-2.1


./configure --with-ld-opt=-Wl,-rpath,/usr/local/lib/ --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module


./configure --with-ld-opt=-Wl,-rpath,/usr/local/lib/ --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module-0.10.7 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module




  nginx path prefix: "/usr/local/nginx"
  nginx binary file: "/usr/local/nginx/sbin/nginx"
  nginx modules path: "/usr/local/nginx/modules"
  nginx configuration prefix: "/usr/local/nginx/conf"
  nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
  nginx pid file: "/usr/local/nginx/logs/nginx.pid"
  nginx error log file: "/usr/local/nginx/logs/error.log"
  nginx http access log file: "/usr/local/nginx/logs/access.log"
  nginx http client request body temporary files: "client_body_temp"
  nginx http proxy temporary files: "proxy_temp"
  nginx http fastcgi temporary files: "fastcgi_temp"
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"





"""