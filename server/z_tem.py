import requests

url = 'https://book.douban.com/tag/%E9%98%BF%E5%8A%A0%E8%8E%8E%C2%B7%E5%85%8B%E9%87%8C%E6%96%AF%E8%92%82'
res = requests.get(url)
print(res.content.decode())



# tee /home/wangqian/tem_data/wangqian_xs_slow_sql.sql
# select * from mysql.slow_log where db='wangqian_xs' order by start_time  DESC limit 300;



# tee /home/wangqian/tem_data/kuaijie_slow_sql.sql
# select * from mysql.slow_log where db='kuaijie' order by start_time  DESC limit 300;




# tee /home/wangqian/tem_data/djangodrug_slow_sql.sql
# select * from mysql.slow_log where db='djangodrug' order by start_time  DESC limit 300;






"""

`start_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `user_host` mediumtext NOT NULL,
  `query_time` time(6) NOT NULL,
  `lock_time` time(6) NOT NULL,
  `rows_sent` int(11) NOT NULL,
  `rows_examined` int(11) NOT NULL,
  `db` varchar(512) NOT NULL,
  `last_insert_id` int(11) NOT NULL,
  `insert_id` int(11) NOT NULL,
  `server_id` int(10) unsigned NOT NULL,
  `sql_text` mediumblob NOT NULL,
  `thread_id` bigint(21) unsigned NOT NULL

"""