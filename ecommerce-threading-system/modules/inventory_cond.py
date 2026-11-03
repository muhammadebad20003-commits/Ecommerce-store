from threading import Thread, Condition
import time

class CheckoutConsumer(Thread):
    def __init__(self, buffer_list, cond):
        super().__init__()
        self.buffer_list = buffer_list
        self.cond = cond

    def run(self):
        for _ in range(3):
            with self.cond:
                if len(self.buffer_list) == 0:
                    print('[Module 2 - Condition] Out of stock! Checkout waiting for restock...')
                    self.cond.wait()
                self.buffer_list.pop()
                print('[Module 2 - Condition] Order checked out, 1 item dispatched.')
                self.cond.notify()
            time.sleep(0.8)

class RestockProducer(Thread):
    def __init__(self, buffer_list, cond):
        super().__init__()
        self.buffer_list = buffer_list
        self.cond = cond

    def run(self):
        for _ in range(3):
            with self.cond:
                if len(self.buffer_list) == 5:
                    print('[Module 2 - Condition] Shelf full (5 items). Restock paused.')
                    self.cond.wait()
                self.buffer_list.append(1)
                print(f'[Module 2 - Condition] Restocked 1 item. Current buffer: {len(self.buffer_list)}')
                self.cond.notify()
            time.sleep(0.4)

def run_inventory_condition():
    buffer = []
    cond = Condition()
    cons = CheckoutConsumer(buffer, cond)
    prod = RestockProducer(buffer, cond)
    cons.start(); prod.start()
    cons.join(); prod.join()