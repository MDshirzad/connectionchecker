from icmplib import ping
from time import sleep

host=input("Enter the server url or ip: ")

while 1:
	
	res= ping(host, count=1,interval=2,timeout=0.3)
	avg=res.avg_rtt
	if(int(avg)-1<0):
		print("connection lost")  
	else:
		print(avg)
	sleep(0.05) #sleep time
