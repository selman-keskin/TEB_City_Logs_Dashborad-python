FROM python

ADD kafka_producer.py /

RUN pip install kafka-python

CMD [ "python", "./kafka_producer.py" ]