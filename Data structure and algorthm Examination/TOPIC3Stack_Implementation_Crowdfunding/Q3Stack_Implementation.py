class StartupNode:
    def __init__(self, name, funding_goal, raised_amount, description):
        self.name, self.funding_goal, self.raised_amount, self.description = name, funding_goal, raised_amount, description

class StartupStack:
    def __init__(self):
        self.stack = []
    
    def push(self, startup):
        self.stack.append(startup)
        print(f"Startup '{startup.name}' added to the stack.")
    
    def pop(self):
        if self.stack:  # Check if stack is not empty
            print(f"Startup '{self.stack.pop().name}' removed from the stack.")
        else:
            print("No startups in the stack.")
    
    def peek(self):
        if self.stack: return self.stack[-1]
        print("No startups in the stack.")
        return None
    
    def is_empty(self):
        return not self.stack
    
    def display_stack(self):
        if not self.stack: print("\nNo startups are currently being processed.")
        else:
            print("\nStartups in the processing stack:")
            for startup in reversed(self.stack):
                print(f"\nStartup Name: {startup.name}, Funding Goal: {startup.funding_goal}, Raised Amount: {startup.raised_amount}, Description: {startup.description}")

if __name__ == "__main__":
    platform_stack = StartupStack()

    # Create startup instances
    startup1 = StartupNode("Rwanda Energy Access", 500000, 250000, "Rwanda Energy Access and Quality Improvement Project.")
    startup2 = StartupNode("Digital Ambassadors Programme", 300000, 150000, "Increasing citizens’ literacy in ICT.")
    startup3 = StartupNode("Second Rwanda Urban Development Programme", 1000000, 700000, "Provide basic infrastructures in secondary cities.")

    # Push, display, pop, and check stack
    platform_stack.push(startup1)
    platform_stack.push(startup2)
    platform_stack.push(startup3)
    platform_stack.display_stack()

    print(f"\nCurrently processing: {platform_stack.peek().name if platform_stack.peek() else 'No startups in the stack.'}")
    
    platform_stack.pop()
    platform_stack.display_stack()

    print("\nNo startups in the processing queue." if platform_stack.is_empty() else "\nThere are startups in the processing queue.")
