import threading
import time

def payment_microservice():
    print(threading.currentThread().getName() + ' --> Payment Gateway microservice starting...')
    time.sleep(0.5)
    print(threading.currentThread().getName() + ' --> Payment Gateway online.')

def inventory_microservice():
    print(threading.currentThread().getName() + ' --> Inventory Sync microservice starting...')
    time.sleep(0.5)
    print(threading.currentThread().getName() + ' --> Inventory Sync online.')

def run_microservices():
    micro1 = Thread(name='PaymentService', target=payment_microservice)
    micro2 = Thread(name='InventoryService', target=inventory_microservice)
    micro1.start(); micro2.start()
    micro1.join(); micro2.join()