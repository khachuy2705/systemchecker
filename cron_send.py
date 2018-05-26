import config
from epayfunc import *

def notiworker(it):
	try:
		if llen(config.redis_key_notify) > 0:
			tmpmsg=lpop(key=config.redis_key_notify).split('|-|')
			# print(tmpmsg.decode("utf-8"))
			# print(type(tmpmsg[0]))
			# thoigian=int(tmpmsg[0])
			# if tmpmsg[0]-getnow('int') >=59:
			# print(int(tmpmsg[0]) - getnow('int'))
			if getnow('int')-int(tmpmsg[0]) <= config.message_timeout:
				# print(tmpmsg)
				# print(int(tmpmsg[0])-getnow('int'))
				mail(config.list_email,'[Systemc checker] - Canh bao su co',tmpmsg[1])
				telegram_send(tmpmsg[1])
			return True
		else:
			return False
	except Exception as values:
		print(values)
		write_log(values)
		# print('Co loi trong qua trinh gui mail')

import threading
thread_count = 5
for i in range(thread_count):
	t = threading.Thread(target=notiworker, args = ('it',))
	t.start()
