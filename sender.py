#!/usr/bin/env python
import pika
import dotenv
import os

dotenv.load_dotenv()

BROKER_IP = os.environ.get('BROKER_IP')
QUEUE_NAME = os.environ.get('QUEUE_NAME')
EXCHANGE = os.environ.get('EXCHANGE')
assert BROKER_IP is not None
assert QUEUE_NAME is not None
assert EXCHANGE is not None

def main():
  assert BROKER_IP is not None
  assert QUEUE_NAME is not None
  assert EXCHANGE is not None
  connection = pika.BlockingConnection(pika.ConnectionParameters(BROKER_IP))
  channel = connection.channel()
  channel.exchange_declare(exchange=EXCHANGE)
  channel.queue_declare(queue=QUEUE_NAME)

  channel.basic_publish(exchange=EXCHANGE,
                      routing_key='r1',
                      body='Hello World!')
  print(" [x] Sent 'Hello World!'")
  connection.close()


main()