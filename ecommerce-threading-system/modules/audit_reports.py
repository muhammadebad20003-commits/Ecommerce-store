from threading import Thread

def audit_task(thread_number):
    print(f'[Module 9 - Sequential Join] Generating department audit report #{thread_number}')

def run_audit_loop():
    for i in range(3):
        t = Thread(target=audit_task, args=(i,))
        t.start()
        t.join()