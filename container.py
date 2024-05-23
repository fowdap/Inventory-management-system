import threading

# container class 

class Container:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_items = 0
        self.container_number = 1
        self.lock = threading.Lock()

    def add_item(self):
        with self.lock:
            if self.current_items < self.capacity:
                self.current_items += 1
                print(f"Added item to container, current items in a container: {self.current_items}")
            else:
                print("Container is full. Switching to new container.")
                self.container_number += 1
                self.current_items = 1  # Start new container
                print(f"New container started, current items: {self.current_items}")
                print(f"Loading on {self.container_number}")

    def get_current_items(self):
        with self.lock:
            return self.current_items
