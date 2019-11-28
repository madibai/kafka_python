from pykafka import KafkaClient
from kafka import KafkaProducer
from time import sleep

#client = KafkaClient(hosts='127.0.0.1:9092',use_greenlets=True)
#topic = client.topics['first_topic']
#producer = topic.get_producer()
prod = KafkaProducer(bootstrap_servers=['localhost:9092'])
count = 1
while count<3:
    message = ('Hello Altuwa '+str(count)).encode('ascii')
    prod.send('python-topic',message)
    sleep(10)
    count += 1
prod.close()