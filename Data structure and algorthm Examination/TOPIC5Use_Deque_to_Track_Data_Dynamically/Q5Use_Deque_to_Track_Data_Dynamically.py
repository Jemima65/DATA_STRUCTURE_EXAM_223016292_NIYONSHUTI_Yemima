from collections import deque

class StartupTrackingDeque:
    def __init__(self, max_size):
        self.startups = deque(maxlen=max_size)

    def add_startup(self, name, funding_goal, raised_amount, description):
        self.startups.append((name, funding_goal, raised_amount, description))
        print(f"Startup '{name}' added for tracking.")

    def update_funding(self, name, new_raised_amount):
        for i, (startup_name, funding_goal, raised_amount, description) in enumerate(self.startups):
            if startup_name == name:
                self.startups[i] = (startup_name, funding_goal, new_raised_amount, description)
                print(f"Funding for '{name}' updated to {new_raised_amount}.")
                return
        print(f"Startup '{name}' not found for update.")

    def remove_startup(self, name):
        for i, (startup_name, _, _, _) in enumerate(self.startups):
            if startup_name == name:
                self.startups.remove(self.startups[i])
                print(f"Startup '{name}' removed from tracking.")
                return
        print(f"Startup '{name}' not found for removal.")

    def display_startups(self):
        if not self.startups:
            print("No startups currently being tracked.")
            return
        print("\nStartups being tracked:")
        for name, funding_goal, raised_amount, description in self.startups:
            print(f"\nStartup Name: {name}, Funding Goal: {funding_goal}, Raised Amount: {raised_amount}, Description: {description}")

    def peek_front(self):
        if self.startups:
            name, funding_goal, raised_amount, description = self.startups[0]
            print(f"\nFront of the deque: {name}, Funding Goal: {funding_goal}, Raised Amount: {raised_amount}")
        else:
            print("No startups in the deque.")

    def peek_rear(self):
        if self.startups:
            name, funding_goal, raised_amount, description = self.startups[-1]
            print(f"\nRear of the deque: {name}, Funding Goal: {funding_goal}, Raised Amount: {raised_amount}")
        else:
            print("No startups in the deque.")

# Example usage
if __name__ == "__main__":
    platform = StartupTrackingDeque(3)  # Track up to 3 startups at a time

    # Add some startups
    platform.add_startup("Rwanda Energy Access", 500000, 250000, "Rwanda Energy Access and Quality Improvement Project.")
    platform.add_startup("Digital Ambassadors Programme", 300000, 150000, "Increasing citizens’ literacy in ICT.")
    platform.add_startup("Second Rwanda Urban Development Programme", 1000000, 700000, "Provide basic infrastructures in secondary cities.")
    
    platform.display_startups()  # Display current startups being tracked

    # Add a new startup, this will remove the oldest one (due to deque size limit)
    platform.add_startup("New Green Initiative", 400000, 200000, "Green energy solutions for Rwanda.")
    platform.display_startups()  # Display startups after new addition

    # Update funding for a startup
    platform.update_funding("Digital Ambassadors Programme", 180000)
    
    # Peek at the front and rear startups
    platform.peek_front()
    platform.peek_rear()

    # Remove a startup from tracking
    platform.remove_startup("Second Rwanda Urban Development Programme")
    platform.display_startups()  # Display remaining startups