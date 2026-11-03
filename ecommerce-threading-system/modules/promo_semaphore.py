from threading import Thread, Semaphore
import random
import time

def customer_voucher_waiter(sem, get_code_func):
    print('[Module 8 - Semaphore] Customer waiting for discount code...')
    sem.acquire()
    print(f'[Module 8 - Semaphore] Voucher received! Code: {get_code_func()}')

def admin_voucher_generator(sem, set_code_func):
    time.sleep(1)
    code = random.randint(10000, 99999)
    set_code_func(code)
    print(f'[Module 8 - Semaphore] Admin generated flash voucher: {code}')
    sem.release()

def run_promo_semaphore():
    voucher_semaphore = Semaphore(0)
    current_voucher = [0]
    get_v = lambda: current_voucher[0]
    set_v = lambda val: current_voucher.__setitem__(0, val)
    v_cust = Thread(target=customer_voucher_waiter, args=(voucher_semaphore, get_v))
    v_admin = Thread(target=admin_voucher_generator, args=(voucher_semaphore, set_v))
    v_cust.start(); v_admin.start()
    v_cust.join(); v_admin.join()