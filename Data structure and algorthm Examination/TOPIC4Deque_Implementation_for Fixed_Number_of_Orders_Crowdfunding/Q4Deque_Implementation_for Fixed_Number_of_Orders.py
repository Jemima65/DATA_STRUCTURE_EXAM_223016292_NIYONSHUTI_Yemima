from collections import deque

class OrderDeque:
    def __init__(self, max_size):
        self.orders = deque(maxlen=max_size)

    def add_order(self, name, amount):
        self.orders.append((name, amount))
        print(f"Order for '{name}' with amount {amount} added to the deque.")

    def remove_order(self):
        if self.orders:
            name, _ = self.orders.popleft()
            print(f"Order for '{name}' processed and removed from the deque.")
        else:
            print("No orders to process.")

    def display_orders(self):
        if self.orders:
            print("\nOrders in the crowdfunding platform:")
            for name, amount in self.orders:
                print(f"Startup Name: {name}, Order Amount: {amount}")
        else:
            print("\nNo orders in the deque.")

    def peek_front(self):
        if self.orders:
            name, amount = self.orders[0]
            print(f"Order at the front: {name}, Amount: {amount}")
    
    def peek_rear(self):
        if self.orders:
            name, amount = self.orders[-1]
            print(f"Order at the rear: {name}, Amount: {amount}")

# Example usage
if __name__ == "__main__":
    platform = OrderDeque(3)

    platform.add_order("Rwanda Energy Access", 50000)
    platform.add_order("Digital Ambassadors Programme", 30000)
    platform.add_order("Second Rwanda Urban Development Programme", 70000)
    
    platform.display_orders()

    platform.add_order("New Green Initiative", 40000)  # Will remove the oldest order
    platform.display_orders()

    platform.peek_front()
    platform.peek_rear()

    platform.remove_order()  # Removes the front order
    platform.display_orders()

