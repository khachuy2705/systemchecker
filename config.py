#-*- coding: utf-8 -*-
########################################################################
#Danh sách cần check:
list_check_port=[
	'google.com.vn:80',
	'genk.vn:443',
	'dantri.vn:80'
]

list_check_ping=[
	'8.8.8.8',
	'8.8.4.4',
	'4.2.2.3',
	'4.2.2.4'
]

list_url=[
	'http://congcaphe.com',
	'http://dantri.com.vn',
	'https://www.foody.vn'
]
########################################################################
#Danh sách email nhận cảnh báo
list_email=[
	'funny2705@gmail.com',
	'homthucuatao1@gmail.com'
]
########################################################################
#Cấu hình telegram
api_telegram = 'api'
chat_id_telegram = '***'

#Cấu hình log file
log_file='debug.log'

########################################################################
#Cấu hình kết nối tới redis

#cho_phep_su_dung_redis nếu bằng 1 thì mới cần redis để gửi notify, nếu không tiện triển khai redis thì bỏ qua, chỉ cần 1 server thực hiện check + alert
cho_phep_su_dung_redis='1'
redis_host='127.0.0.1'
redis_port=6379
redis_password=None
import redis
redis = redis.Redis(host=redis_host, port=redis_port, db=0, password=redis_password, connection_pool=None)
#tên key gắn vào list notify, các thông báo message cần gửi được gắn vào list này
redis_key_notify='buikhachuy2705keychoredis_notify'
#Thời gian tối đa tồn tại tối đa của 1 message tình theo giây, thời gian xử lý - thời gian đưa lên < message_timeout mới chấp nhận gửi đi.
message_timeout=60
########################################################################
Nooij