import threading

# Production class   

class Production:
    def __init__(self):
        self.total_produced = 0
        self.total_remaining = 0
        self.lock = threading.Lock()

    def produce(self):
        self.total_produced += 1
        print(f"total produced: {self.total_produced}")
        return self.total_produced

    def add_to_stock(self):
        with self.lock:
            self.total_remaining += 1
            print(f"total remaining in the stock: {self.total_remaining}")

    def remove_item(self):
        with self.lock:
            self.total_remaining -= 1

    def get_total_remaining(self):
        with self.lock:
            return self.total_remaining
