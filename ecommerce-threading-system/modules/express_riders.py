from threading import Thread

class ExpressDeliveryThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"[Module 11 - Custom Thread] Express rider dispatched for order: {self.name}")

def run_express_riders():
    d_rider = ExpressDeliveryThread("Order_#9981")
    d_rider.start(); d_rider.join()