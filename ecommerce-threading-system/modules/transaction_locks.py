from threading import Thread, Lock
import os
import time

class LedgerTransactionThread(Thread):
    def __init__(self, name, duration, lock):
        super().__init__()
        self.name = name
        self.duration = duration
        self.lock = lock

    def run(self):
        with self.lock:
            print(f"---> [Module 5 - Full Lock] {self.name} updating financial ledger, PID: {os.getpid()}")
            time.sleep(self.duration)
            print(f"---> [Module 5 - Full Lock] {self.name} ledger committed.")

class FastCheckoutThread(Thread):
    def __init__(self, name, duration, lock):
        super().__init__()
        self.name = name
        self.duration = duration
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print(f"---> [Module 6 - Early Release Lock] {self.name} locked counter, PID: {os.getpid()}")
        self.lock.release()  # Early release before sleep
        time.sleep(self.duration)
        print(f"---> [Module 6 - Early Release Lock] {self.name} digital receipt printed.")

def run_transaction_locks():
    ledger_lock = Lock()
    fast_lock = Lock()
    l1 = LedgerTransactionThread("LedgerTask", 1, ledger_lock)
    f1 = FastCheckoutThread("FastCounter", 1, fast_lock)
    l1.start(); f1.start()
    l1.join(); f1.join()