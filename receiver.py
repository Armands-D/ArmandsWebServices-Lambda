#!/usr/bin/env python
import pika
import dotenv
import sys, os
import time
import signal

dotenv.load_dotenv()

def stop_signal_callback(signal, frame):
    print('Signal Ended')
    sys.exit(0)
    ...


BROKER_IP = os.environ.get('BROKER_IP')
QUEUE_NAME = os.environ.get('QUEUE_NAME')
EXCHANGE = os.environ.get('EXCHANGE')
assert BROKER_IP is not None
assert QUEUE_NAME is not None
assert EXCHANGE is not None

def callback(ch, method, properties, body):
    print(f" [y] Received {body}")

def main():
  print('RECV RUNNING...')
  assert BROKER_IP is not None
  assert QUEUE_NAME is not None
  assert EXCHANGE is not None
  connection = pika.BlockingConnection(pika.ConnectionParameters(BROKER_IP))
  channel = connection.channel()

  channel.exchange_declare(exchange=EXCHANGE)
  result = channel.queue_declare(queue=QUEUE_NAME)

  # Publish / Subscribe
  queue_name = result.method.queue
  channel.queue_bind(exchange=EXCHANGE, queue=queue_name, routing_key='r1')

  channel.basic_consume(queue=QUEUE_NAME,
                      auto_ack=True,
                      on_message_callback=callback)
  channel.start_consuming()

def test():
  while True:
      print('RUNNING...')
      time.sleep(1)
    

# Shutdown listener
if __name__ == '__main__':
    signal.signal(signal.SIGTERM, stop_signal_callback)
    signal.signal(signal.SIGKILL, stop_signal_callback)
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)