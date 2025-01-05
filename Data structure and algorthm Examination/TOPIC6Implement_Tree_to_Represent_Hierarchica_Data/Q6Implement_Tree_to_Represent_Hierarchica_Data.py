class StartupNode:
    def __init__(self, name, funding_goal, raised_amount, description):
        self.name = name
        self.funding_goal = funding_goal
        self.raised_amount = raised_amount
        self.description = description
        self.children = []  # List to store child startups (sub-projects)

    def add_child(self, child_node):
        """Add a sub-startup to the current startup node."""
        self.children.append(child_node)

    def remove_child(self, name):
        """Remove a sub-startup by name."""
        self.children = [child for child in self.children if child.name != name]

    def display(self, level=0):
        """Display the startup and its children (sub-projects) in a hierarchical manner."""
        print(f"{'  ' * level}Startup: {self.name}, Funding Goal: {self.funding_goal}, Raised: {self.raised_amount}, {self.description}")
        for child in self.children:
            child.display(level + 1)

class StartupTree:
    def __init__(self, root):
        self.root = root  # The root node represents the main startup

    def add_startup(self, parent_name, child_node):
        """Add a new sub-startup under the parent startup."""
        parent = self.search_startup(self.root, parent_name)
        if parent:
            parent.add_child(child_node)
            print(f"Child startup '{child_node.name}' added under '{parent_name}'")
        else:
            print(f"Parent startup '{parent_name}' not found.")

    def search_startup(self, current_node, name):
        """Search for a startup by its name."""
        if current_node.name == name:
            return current_node
        for child in current_node.children:
            found = self.search_startup(child, name)
            if found:
                return found
        return None  # If not found

    def remove_startup(self, parent_name, child_name):
        """Remove a sub-startup from a parent startup."""
        parent = self.search_startup(self.root, parent_name)
        if parent:
            parent.remove_child(child_name)
            print(f"Child startup '{child_name}' removed from '{parent_name}'")
        else:
            print(f"Parent startup '{parent_name}' not found.")

    def display_startups(self):
        """Display the entire tree of startups (hierarchical structure)."""
        self.root.display()


# Example usage
if __name__ == "__main__":
    # Create the root startup (main project)
    root_startup = StartupNode("Rwanda Energy Access", 500000, 250000, "Improving energy access and quality in Rwanda.")

    # Create a tree structure to manage the startups
    startup_tree = StartupTree(root_startup)

    # Add sub-startups (child nodes)
    child1 = StartupNode("Digital Ambassadors Programme", 300000, 150000, "Promoting ICT literacy among citizens.")
    child2 = StartupNode("Second Rwanda Urban Development Programme", 1000000, 700000, "Developing infrastructure in secondary cities.")
    
    startup_tree.add_startup("Rwanda Energy Access", child1)
    startup_tree.add_startup("Rwanda Energy Access", child2)

    # Add further child to a sub-startup to create a deeper hierarchy
    sub_child1 = StartupNode("ICT for Rural Areas", 150000, 80000, "Providing ICT education to rural communities.")
    startup_tree.add_startup("Digital Ambassadors Programme", sub_child1)

    # Display the hierarchical tree of startups
    print("\nAll Startups in the Platform (Hierarchical Structure):")
    startup_tree.display_startups()

    # Search for a specific startup in the tree
    found_startup = startup_tree.search_startup(startup_tree.root, "ICT for Rural Areas")
    if found_startup:
        print(f"\nFound Startup: {found_startup.name}, Funding Goal: {found_startup.funding_goal}")

    # Remove a child startup
    startup_tree.remove_startup("Rwanda Energy Access", "Digital Ambassadors Programme")

    # Display the tree after removing a sub-startup
    print("\nAfter Removal of 'Digital Ambassadors Programme':")
    startup_tree.display_startups()

