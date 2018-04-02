from epayfunc import *
from config import list_check_port as list_check_port
from config import list_check_ping as list_check_ping
from config import list_url as list_url

# for member in list_check_port:
# 	host_temp=member.split(':')
# 	result=check_port(host=host_temp[0],port=host_temp[1])
# 	if result[0]==0:
# 		mail()

def check_port_list(lists):
	"""check list port sau do canh bao"""
	for tmp in lists:
		host_tmp=tmp.split(':')
		result=check_port(host=host_tmp[0],port=host_tmp[1])
		if result[0]==0:
			mail(config.list_email,'Canh bao check port that bai',result[1])
			telegram_send(result[1])
		else:
			continue

def check_ping_list(lists):
	"""Check list cac host can ping, sau do canh bao"""
	for tmp in lists:
		result=check_ping(tmp)
		if result[0]==0:
			mail(config.list_email,'Canh bao check ping that bai',result[1])
			telegram_send(result[1])
		else:
			continue

check_ping_list(config.list_check_ping)
check_port_list(config.list_check_port)