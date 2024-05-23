import threading

# robot class

class Robot:
    def __init__(self, name, production, container):
        self.name = name
        self.items_picked = 0
        self.items_transferred = 0
        self.production = production
        self.container = container
        self.lock = threading.Lock()

    def pick_up(self):
        with self.lock:
            if self.production.get_total_remaining() > 0:
                self.items_picked += 1
                self.production.remove_item()
                print(f"{self.name} picked")

    def transferred(self):
        with self.lock:
            self.items_transferred += 1
            self.container.add_item()
            print(f"{self.name} transferred")
