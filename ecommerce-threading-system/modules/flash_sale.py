from threading import Barrier, Thread
import random
import time

def flash_sale_node(warehouses_list, barrier):
    name = warehouses_list.pop()
    time.sleep(random.randrange(1, 3))
    print(f"[Module 1 - Barrier] {name} cache synced.")
    barrier.wait()
    print(f"*** [Module 1 - Barrier] {name} LIVE! Flash sale orders rolling! ***\n")

def run_flash_sale():
    warehouses_pool = ['North_Warehouse', 'Central_Warehouse', 'South_Warehouse']
    barrier = Barrier(len(warehouses_pool))
    threads = [Thread(target=flash_sale_node, args=(warehouses_pool, barrier)) for _ in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()