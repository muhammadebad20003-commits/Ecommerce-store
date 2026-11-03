import sys
import os

# Modules folder ko path mein include karna
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from modules.flash_sale import run_flash_sale
from modules.inventory_cond import run_inventory_condition
from modules.order_event import run_order_event
from modules.suppliers import run_suppliers
from modules.transaction_locks import run_transaction_locks
from modules.warehouse_rlock import run_warehouse_rlock
from modules.promo_semaphore import run_promo_semaphore
from modules.audit_reports import run_audit_loop
from modules.microservices import run_microservices
from modules.express_riders import run_express_riders  # <-- Yahan run_express_riders hona chahiye
from modules.order_queue import run_order_queue

def main():
    print("==================================================")
    print("  E-COMMERCE CONCURRENCY SYSTEM (MODULAR STRUCTURE)")
    print("==================================================\n")

    print(">> Executing Module 1: Flash Sale Synchronization")
    run_flash_sale()
    print("-" * 50)

    # Baaki modules ke calls...
    print(">> Executing Module 11: Express Delivery Custom Threads")
    run_express_riders() # <-- Yahan bhi sahi function call ho
    print("-" * 50)

if __name__ == "__main__":
    main()