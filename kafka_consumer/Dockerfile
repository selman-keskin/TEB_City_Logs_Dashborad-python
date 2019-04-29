FROM python

ADD kafka_consumer.py /

RUN pip install kafka-python

RUN pip install elasticsearch

CMD [ "python", "./kafka_consumer.py" ]