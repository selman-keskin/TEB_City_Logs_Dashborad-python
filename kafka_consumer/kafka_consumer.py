import sys
import time
from kafka import KafkaConsumer
from json import loads
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': '192.168.0.101', 'port': 9200}])
doc_id = 0

#es.indices.create(index = 'logs-index')
#es.indices.put_mapping(
#    index="logs-index",
#    doc_type="log",
#    body={
#        "properties": {
#     
#            "id": {"type": "long"},
#            "@timestamp": {"type":"date"},  #, "ignore_malformed": "true"},
#            "log_level": {"type": "text"},
#            "log_server_city_name": {"type": "text"},
#            "log_detail": {"type": "text"}
#
#        }
#    }
#)

consumer = KafkaConsumer(
    'city_logs',
     bootstrap_servers=['192.168.0.100:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(message)

    message = message.split('\t')

    message[0]=message[0].split(' ')
    timestamp = message[0][0]+'T'+message[0][1]+'Z'

    doc_id = doc_id + 1
    doc = {
    'id': doc_id,
    'timestamp': timestamp,
    'log_level': message[1],
    'log_server_city_name': message[2],
    'log_detail': message[3] }

    res = es.index(index = "logs-index", doc_type = 'log', id = doc_id, body = doc)