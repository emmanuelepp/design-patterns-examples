# Proxy:
# Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object,
# allowing you to perform something either before or after the request gets through to the original object.

import time


class Producer:

    def producer(self):
        print('working...')

    def meet(self):
        print('Nice to meet you!')


class Proxy:
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        print('Checking is producer is avaible...')

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()
        else:
            time.sleep(2)
            print('Producer busy')


# Instantiate
proxy = Proxy()
# Make the proxy
proxy.produce()
# Change the state
proxy.occupied = 'Yes'
# Make the producer
proxy.produce()
