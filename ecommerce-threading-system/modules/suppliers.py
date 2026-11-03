from threading import Thread
import os
import time

class SupplierBatchThread(Thread):
    def __init__(self, name, duration):
        super().__init__()
        self.name = name
        self.duration = duration

    def run(self):
        print(f"---> [Module 4 - Custom Thread] {self.name} processing bulk supply, Process ID: {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> [Module 4 - Custom Thread] {self.name} shipment completed.\n")

def run_suppliers():
    s1 = SupplierBatchThread("Supplier_A", 1)
    s2 = SupplierBatchThread("Supplier_B", 1)
    s1.start(); s2.start()
    s1.join(); s2.join()