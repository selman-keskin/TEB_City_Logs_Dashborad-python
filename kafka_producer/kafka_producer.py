from os import listdir
from os.path import isfile, join
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['192.168.0.100:9092'],
						 api_version=(0,10),
						 acks='all',
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

#mypath = '/var/lib/docker/volumes/logs/_data/'
mypath = '/logs/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(len(onlyfiles))

for var in range(len(onlyfiles)):
	file_name =  'log' + str(var) + '.csv'
	with open(mypath + file_name) as file:
		for line in file:
			print(line)
			producer.send('city_logs',value=line)