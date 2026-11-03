from threading import Thread, Event
import random
import time

class PackagingWorker(Thread):
    def __init__(self, cart_list, ev):
        super().__init__()
        self.cart_list = cart_list
        self.ev = ev

    def run(self):
        time.sleep(1)
        self.ev.wait()
        if self.cart_list:
            item_id = self.cart_list.pop()
            print(f'📦 [Module 3 - Event] Packaging daemon packed order #{item_id} by {self.name}')

class PaymentGateway(Thread):
    def __init__(self, cart_list, ev):
        super().__init__()
        self.cart_list = cart_list
        self.ev = ev

    def run(self):
        time.sleep(0.5)
        item_id = random.randint(1000, 9999)
        self.cart_list.append(item_id)
        print(f'💳 [Module 3 - Event] Payment received for order #{item_id} by {self.name}')
        self.ev.set()
        self.ev.clear()

def run_order_event():
    cart = []
    event = Event()
    worker = PackagingWorker(cart, event)
    worker.name = "Packer"
    gateway = PaymentGateway(cart, event)
    gateway.name = "Gateway"
    worker.start(); gateway.start()
    worker.join(); gateway.join()