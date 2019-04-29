import os
import sys
import random
import datetime

if len(sys.argv) != 2:
	print('Usage: log_producer.py <log_number>')
	quit()
	
log_number = sys.argv[1]

list1 = ['INFO', 'WARN', 'FATAL', 'DEBUG', 'ERROR']
list2 = ['Istanbul\tHello-from-Istanbul','Tokyo\tHello-from-Tokyo','Moskow\tHello-from-Moskow','Beijing\tHello-from-Beijing','London\tHello-from-London']

for var in list(range(int(log_number))):
	new_path = os.getcwd() + '/logs/'+ 'log' + str(var) + '.csv'
	files = open(new_path,'w')
	
	while True:
		datetime_object = datetime.datetime.now()
		files.write(str(datetime_object)[:-3] + '\t' + list1[random.randint(0,4)] + '\t' + list2[random.randint(0,4)] + '\n')
		statinfo = os.stat(new_path)

		print(new_path + '\t' + str(statinfo.st_size))
		if int(statinfo.st_size) >= 2*1024*1024:
			files.close()
			break