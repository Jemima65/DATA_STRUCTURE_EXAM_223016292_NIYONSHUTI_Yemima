class Startup:
    def __init__(self, name, funding_goal, raised_amount, description):
        self.name, self.funding_goal, self.raised_amount, self.description = name, funding_goal, raised_amount, description
    def __repr__(self): return f"Startup(name={self.name}, funding_goal={self.funding_goal}, raised_amount={self.raised_amount}, description={self.description})"

def merge_sort(startups, key):
    if len(startups) <= 1: return startups
    mid = len(startups) // 2
    return merge(merge_sort(startups[:mid], key), merge_sort(startups[mid:], key), key)

def merge(left, right, key):
    sorted_list = []
    while left and right:
        sorted_list.append(left.pop(0) if getattr(left[0], key) <= getattr(right[0], key) else right.pop(0))
    return sorted_list + left + right

# Example Usage
if __name__ == "__main__":
    startups = [Startup("Rwanda Energy Access", 500000, 250000, "Energy access in Rwanda."),
                Startup("Digital Ambassadors Programme", 300000, 150000, "Increasing ICT literacy."),
                Startup("Second Rwanda Urban Development Programme", 1000000, 700000, "Infrastructure development."),
                Startup("Eco Friendly Tech", 400000, 350000, "Green technology solutions."),
                Startup("Tech Innovators", 600000, 450000, "Tech solutions for the future.")]
                
    for key in ["funding_goal", "raised_amount"]:
        print(f"Sorting by {key}:")
        for startup in merge_sort(startups, key):
            print(startup)
        print()
