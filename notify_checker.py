#-*- coding: utf-8 -*-
from epayfunc import *

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

def check_link_lists(lists):
	"""Check cac link được cấu hình trong config.py"""
	for tmp in lists:
		result=http_check(tmp)
		if result[0]==0:
			mail(config.list_email,'Canh bao check ping that bai',result[1])
			telegram_send(result[1])
		else:
			continue

import threading
if check_internet():
	linkck = threading.Thread(target=check_link_lists, args=(config.list_url,))
	pingck = threading.Thread(target=check_ping_list, args=(config.list_check_ping,))
	portck = threading.Thread(target=check_port_list, args=(config.list_check_port,))
	linkck.start()
	pingck.start()
	portck.start()
	linkck.join()
	pingck.join()
	portck.join()
	# check_link_lists(config.list_url)
	# check_ping_list(config.list_check_ping)
	# check_port_list(config.list_check_port)