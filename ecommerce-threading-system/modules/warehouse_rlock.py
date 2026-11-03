from threading import Thread, RLock
import time

class WarehouseBox:
    def __init__(self):
        self.lock = RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def bin_adder(box, items):
    print(f"[Module 7 - Rlock] Adding {items} items to warehouse bin...")
    while items > 0:
        box.add()
        time.sleep(0.2)
        items -= 1

def bin_remover(box, items):
    print(f"[Module 7 - Rlock] Removing {items} items from warehouse bin...")
    while items > 0:
        box.remove()
        time.sleep(0.2)
        items -= 1

def run_warehouse_rlock():
    box = WarehouseBox()
    t_add = Thread(target=bin_adder, args=(box, 5))
    t_rem = Thread(target=bin_remover, args=(box, 3))
    t_add.start(); t_rem.start()
    t_add.join(); t_rem.join()
    print(f"Final Warehouse Bin Item Count: {box.total_items}")