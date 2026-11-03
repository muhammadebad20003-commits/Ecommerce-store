from threading import Thread
from queue import Queue
import random
import time

class OrderQueueProducer(Thread):
    def __init__(self, q, name):
        super().__init__(name=name)
        self.queue = q
    def run(self):
        for _ in range(2):
            item = random.randint(100, 999)
            self.queue.put(item)
            print(f'🛒 [Module 12 - Queue] Customer cart #{item} added to queue by {self.name}')
            time.sleep(0.3)

class OrderQueueConsumer(Thread):
    def __init__(self, q, name):
        super().__init__(name=name)
        self.queue = q
    def run(self):
        while not self.queue.empty():
            item = self.queue.get()
            print(f'📦 [Module 12 - Queue] Fulfillment worker packed cart #{item} ({self.name})')
            self.queue.task_done()

def run_order_queue():
    q = Queue()
    prod = OrderQueueProducer(q, name="CartTaker")
    cons = OrderQueueConsumer(q, name="PackerWorker")
    prod.start(); prod.join()
    cons.start(); cons.join()