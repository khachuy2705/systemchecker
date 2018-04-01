#Cấu hình telegram
api_telegram = 'https://api.telegram.org/bot471775980:AAGtU-QXFQfYmyfvatdUAwMB2XWzRc8F6EE/sendMessage'
chat_id_telegram = '428519060'

#Cấu hình log file
log_file='debug.log'

########################################################################
#Cấu hình kết nối tới redis
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
