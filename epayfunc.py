#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# coding=utf-8
import config
from config import redis as redis
#redis.set('genk','huybk',10)

def telegram_send(noi_dung):
	import requests
	header = {'Content-Type': 'application/json'}
	body = """{
			"chat_id":\""""+str(config.chat_id_telegram)+"""\",
			"text":\""""+noi_dung+"""\"
			}"""
	r = requests.post(config.api_telegram, data=body, headers=header, timeout=30)
	return r.content


def mail(nguoi_nhan, tieu_de, noi_dung, username_sender='liles125876@gmail.com', password_sender='khachuy2705'):
	import smtplib
	TO = nguoi_nhan
	SUBJECT = tieu_de
	TEXT = noi_dung
	# Gmail Sign In
	# gmail_sender = 'liles125876@gmail.com'
	# gmail_passwd = 'khachuy2705'
	gmail_sender = username_sender
	gmail_passwd = password_sender

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_sender, gmail_passwd)

	BODY = '\r\n'.join(['To: %s' % TO,
	                    'From: %s' % gmail_sender,
	                    'Subject: %s' % SUBJECT,
	                    '', TEXT]).encode('utf-8')
	try:
		server.sendmail(gmail_sender, TO.split(','), BODY)
		print('Email da duoc gui di')
	except Exception as values:
		print(values)
		print('Co loi trong qua trinh gui mail')
	server.quit()


def write_log(content):
	import datetime
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S : ')
	try:
		f = open('exec_log.txt', 'a+')
		f.write('\n')
		f.write(str(now)+' : '+content)
		print(str(now)+' : '+content)
	except Exception as vl:
		print('Co loi xay ra trong qua trinh ghi log')
		print(vl)
	finally:
		pass

def check_ping(target):
	import os
	if os.name == 'nt':
		rep = os.system("ping -n 1 " + target + '> nul')
		if rep == 0:
			mess = "Ping " + str(target) + " thanh cong"
			print(mess)
			return [1, mess]
		else:
			mess = "Mat ket noi toi " + target
			print(mess)
			return [0, mess]
	else:
		rep = os.system("ping -c 1 " + target)
		if rep == 0:
			mess = "Ping " + str(target) + " thanh cong"
			print(mess)
			return [1, mess]
		else:
			mess = "Mat ket noi toi " + target
			print(mess)
			return [0, mess]

# def ping_linux(target):
# 	import os
# 	rep = os.system("ping -c 1 " + target)
# 	if rep == 0:
# 		mess="Ping "+str(target)+" thanh cong"
# 		# print(mess)
# 		return [1, mess]
# 	else:
# 		mess="Mat ket noi toi "+target
# 		# print(mess)
# 		return [0, mess]
#
# def ping_windows(target):
# 	import os
# 	rep = os.system("ping -n 1 " + target + '> nul')
# 	if rep == 0:
# 		mess="Ping "+str(target)+" thanh cong"
# 		# print(mess)
# 		return [1, mess]
# 	else:
# 		mess="Mat ket noi toi "+target
# 		# print(mess)
# 		return [0, mess]

def check_port(host, port):
	import socket
	host=str(host)
	port=int(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(10) 
	result = sock.connect_ex((host,port))
	if result == 0:
		mess="Ket noi toi "+host+":"+str(port)+" thanh cong"
		print(mess)
		return [1, mess]
	else:
		mess="Ket noi toi "+host+":"+str(port)+" that bai"
		print(mess)
		return [0, mess]
		
def http_check(url, timeout=30):
	"""url phai co http hoac https ơ dau"""
	import requests
	#headers={'Host':'Gi cung duoc'}
	response=requests.get(url, timeout=timeout)
	if response.status_code == 200:
		mess="Ket noi toi "+url+" thanh cong"
		print(mess)
		return [1, mess]
	else:
		mess = "Ket noi toi " + url + " that bai"
		print(mess)
		return [0, mess]


def check_internet():
	"""tra ve True neu co internet, tra ve fail neu khong co internet"""
	chk=check_ping('8.8.8.8')
	if chk[0]==1:
		return True
	else:
		return False

# def check_ping(target):
# 	import os
# 	if os.name == 'nt':
# 		check=ping_windows(target)
# 	else:
# 		check=ping_linux(target)
# 	return check

#Các chức năng đẩy dữ liệu vào redis
def rpush(content):
	try:
		if config.cho_phep_su_dung_redis == 1:
			write_log('Bat dau push du lieu len redis')
			redis.rpush(config.redis_key_notify, content)
			write_log('Da day du lieu len redis: '+str(content))
			return True
		else:
			return False
	except Exception as value:
		print(value)
		write_log(value)
		return False
def lpop(key=config.redis_key_notify):
	try:
		if config.cho_phep_su_dung_redis == 1:
			write_log('Lay du lieu tu redis (LPOP)')
			data=redis.lpop(key)
			write_log('Du lieu lay tu redis:'+str(data))
			return data
		else:
			return False
	except Exception as value:
		print(value)
		write_log(value)
		data=None
		return data

