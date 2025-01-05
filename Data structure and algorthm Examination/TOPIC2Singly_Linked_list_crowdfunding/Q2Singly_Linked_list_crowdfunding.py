class StartupNode:
    def __init__(self, name, funding_goal, raised_amount, description):
        self.name = name  # Startup name
        self.funding_goal = funding_goal  # Funding goal of the startup
        self.raised_amount = raised_amount  # Amount raised so far
        self.description = description  # Description of the startup
        self.next = None  # Link to the next startup node

class StartupLinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list (empty list)
    
    def add_startup(self, name, funding_goal, raised_amount, description):
        new_node = StartupNode(name, funding_goal, raised_amount, description)
        if not self.head:
            self.head = new_node  # If list is empty, new node becomes the head
        else:
            current = self.head
            while current.next: current = current.next  # Traverse to the last node
            current.next = new_node  # Add new node at the end
    
    def remove_startup(self, name):
        current, previous = self.head, None
        while current and current.name != name:
            previous, current = current, current.next
        
        if current:  # If the startup is found
            if previous: previous.next = current.next  # Remove the node
            else: self.head = current.next  # If it's the first node, update head
        else:
            print(f"Startup with name '{name}' not found.")
    
    def search_startup(self, name):
        current = self.head
        while current:
            if current.name == name: return current  # Return the startup if found
            current = current.next
        return None  # Return None if not found
    
    def display_startups(self):
        current = self.head
        if not current: print("No startups available.")  # If list is empty
        while current:
            print(f"Startup Name: {current.name}\nFunding Goal: {current.funding_goal}\nRaised Amount: {current.raised_amount}\nDescription: {current.description}\n")
            current = current.next

if __name__ == "__main__":
    platform = StartupLinkedList()

    platform.add_startup("Rwanda Energy Access", 500000, 250000, "Rwanda Energy Access and Quality Improvement Project.")
    platform.add_startup("Digital Ambassadors Programme", 300000, 150000, "Increasing citizens’ literacy in ICT.")
    platform.add_startup("Second Rwanda Urban Development Programme", 1000000, 700000, "Provide basic infrastructures in secondary cities.")

    print("All Startups in the Platform:")
    platform.display_startups()

    startup = platform.search_startup("Rwanda Energy Access")
    if startup: print(f"Found startup: {startup.name} - Funding Goal: {startup.funding_goal}")

    platform.remove_startup("Rwanda Energy Access")

    print("\nStartups After Removal:")
    platform.display_startups()

