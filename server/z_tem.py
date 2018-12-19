""" test"""
# yjd nginx config
# 文件路径：/root/nginx
"""


configure arguments: --user=root --group=root --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --http-client-body-temp-path=/var/tmp/nginx/client --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fcgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --with-http_v2_module --with-http_ssl_module --with-stream --with-openssl=../openssl-1.1.0g --with-pcre=../pcre-8.38 --with-pcre-jit --with-zlib=../zlib-1.2.11 --with-http_realip_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_geoip_module

nginx version: nginx/1.10.3
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.1.0g  2 Nov 2017
TLS SNI support enabled
configure arguments:

--user=root
--group=root
--prefix=/usr/share/nginx
--sbin-path=/usr/sbin/nginx
--conf-path=/etc/nginx/nginx.conf
--error-log-path=/var/log/nginx/error.log
--http-log-path=/var/log/nginx/access.log
--pid-path=/var/run/nginx/nginx.pid
--lock-path=/var/lock/nginx.lock
--http-client-body-temp-path=/var/tmp/nginx/client
--http-proxy-temp-path=/var/tmp/nginx/proxy
--http-fastcgi-temp-path=/var/tmp/nginx/fcgi
--http-uwsgi-temp-path=/var/tmp/nginx/uwsgi
--with-http_v2_module
--with-http_ssl_module
--with-stream
--with-openssl=../openssl-1.1.0g
--with-pcre=../pcre-8.38
--with-pcre-jit
--with-zlib=../zlib-1.2.11
--with-http_realip_module
--with-http_gzip_static_module
--with-http_stub_status_module
--with-http_geoip_module

"""


# wq nginx config
# 文件路径：/data/download/nginx-1.11.2
"""
nginx version: nginx/1.11.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-11) (GCC)
built with OpenSSL 1.0.2k  26 Jan 2017
TLS SNI support enabled
configure arguments:
--with-ld-opt=-Wl,
-rpath,/usr/local/lib/
--add-module=../ngx_devel_kit-0.3.0
--add-module=../lua-nginx-module-0.10.7
--with-openssl=../openssl
--with-http_v2_module
--with-http_ssl_module
--with-http_gzip_static_module
--with-http_stub_status_module



./configure --prefix=/usr/local/nginx   --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module


"""



# 135测试更新ninx，wq

"""
wget http://nginx.org/download/nginx-1.14.1.tar.gz
tar -zxvf  nginx-1.14.1.tar.gz

export LUAJIT_LIB=/usr/local/luajit/lib
export LUAJIT_INC=/usr/local/luajit/include/luajit-2.0

# 对openssl 重新编译？
cd ../openssl

更新 lua-nginx-module 包: git clone https://github.com/openresty/lua-nginx-module.git

./configure --prefix=/usr/local/nginx  --with-ld-opt=-Wl,-rpath,/usr/local/lib --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module-0.10.7 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module



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


/etc/nginx/conf.d
"""


# 测试服务器 测试更新ninx， 药监单

"""

configure arguments: --user=root --group=root --prefix=/usr/local/nginx   --lock-path=/var/lock/nginx.lock --http-client-body-temp-path=/var/tmp/nginx/client --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fcgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --with-http_v2_module --with-http_ssl_module --with-stream --with-openssl=../openssl-1.1.0g --with-pcre=../pcre-8.38 --with-pcre-jit --with-zlib=../zlib-1.2.11 --with-http_realip_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_geoip_module



  nginx path prefix: "/usr/local/nginx"
  nginx binary file: "/usr/local/nginx/sbin/nginx"
  nginx modules path: "/usr/local/nginx/modules"
  nginx configuration prefix: "/usr/local/nginx/conf"
  nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
  nginx pid file: "/var/run/nginx/nginx.pid"
  nginx error log file: "/var/log/nginx/error.log"
  nginx http access log file: "/var/log/nginx/access.log"
  nginx http client request body temporary files: "/var/tmp/nginx/client"
  nginx http proxy temporary files: "/var/tmp/nginx/proxy"
  nginx http fastcgi temporary files: "/var/tmp/nginx/fcgi"
  nginx http uwsgi temporary files: "/var/tmp/nginx/uwsgi"
  nginx http scgi temporary files: "scgi_temp"






"""


"""

==== Installing LuaJIT 2.1.0-beta2 to /usr/local ====
mkdir -p /usr/local/bin /usr/local/lib /usr/local/include/luajit-2.1 /usr/local/share/man/man1 /usr/local/lib/pkgconfig /usr/local/share/luajit-2.1.0-beta2/jit /usr/local/share/lua/5.1 /usr/local/lib/lua/5.1
cd src && install -m 0755 luajit /usr/local/bin/luajit-2.1.0-beta2
cd src && test -f libluajit.a && install -m 0644 libluajit.a /usr/local/lib/libluajit-5.1.a || :
rm -f /usr/local/lib/libluajit-5.1.so.2.1.0 /usr/local/lib/libluajit-5.1.so /usr/local/lib/libluajit-5.1.so
cd src && test -f libluajit.so && \
  install -m 0755 libluajit.so /usr/local/lib/libluajit-5.1.so.2.1.0 && \
  ldconfig -n /usr/local/lib && \
  ln -sf libluajit-5.1.so.2.1.0 /usr/local/lib/libluajit-5.1.so && \
  ln -sf libluajit-5.1.so.2.1.0 /usr/local/lib/libluajit-5.1.so || :
cd etc && install -m 0644 luajit.1 /usr/local/share/man/man1
cd etc && sed -e "s|^prefix=.*|prefix=/usr/local|" -e "s|^multilib=.*|multilib=lib|" luajit.pc > luajit.pc.tmp && \
  install -m 0644 luajit.pc.tmp /usr/local/lib/pkgconfig/luajit.pc && \
  rm -f luajit.pc.tmp
cd src && install -m 0644 lua.h lualib.h lauxlib.h luaconf.h lua.hpp luajit.h /usr/local/include/luajit-2.1
cd src/jit && install -m 0644 bc.lua bcsave.lua dump.lua p.lua v.lua zone.lua dis_x86.lua dis_x64.lua dis_arm.lua dis_ppc.lua dis_mips.lua dis_mipsel.lua vmdef.lua /usr/local/share/luajit-2.1.0-beta2/jit
==== Successfully installed LuaJIT 2.1.0-beta2 to /usr/local ====

Note: the development releases deliberately do NOT install a symlink for luajit
You can do this now by running this command (with sudo):

  ln -sf luajit-2.1.0-beta2 /usr/local/bin/luajit

"""


"""


# export LUAJIT_LIB=/usr/local/luajit/lib
# export LUAJIT_INC=/usr/local/luajit/include/luajit-2.0
新版本 lua 测试


export LUAJIT_LIB=/usr/local/lib
export LUAJIT_INC=/usr/local/include/luajit-2.1

./configure --with-ld-opt=-Wl,-rpath,/usr/local/lib/ --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module-0.10.7 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module

./configure --with-ld-opt=-Wl,-rpath,/usr/local/lib/ --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module-0.10.7 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module



./configure --with-ld-opt=-Wl,-rpath,/usr/local/lib/ --add-module=../ngx_devel_kit-0.3.0 --add-module=../lua-nginx-module --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module
"""
