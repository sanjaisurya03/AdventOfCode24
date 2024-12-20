
def can_construct_design(design, patterns, memo=None):
    if memo is None:
        memo = {}
    if design in memo:  # Check memoization to avoid redundant calculations
        return memo[design]
    if not design:  # If the design is empty, it can be constructed
        return True
    for pattern in patterns:
        if design.startswith(pattern):  # If the design starts with this pattern
            # Try to construct the remaining part of the design
            if can_construct_design(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True
    memo[design] = False  # If no combination works, return False
    return False


def count_ways_to_construct(design, patterns, memo=None):
    if memo is None:
        memo = {}
    if design in memo:  # Check memoization to avoid redundant calculations
        return memo[design]
    if not design:  # If the design is empty, there's exactly one way to construct it (do nothing)
        return 1

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):  # If the design starts with this pattern
            # Count ways to construct the remaining part of the design
            total_ways += count_ways_to_construct(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways  # Store the result in memo
    return total_ways


def calculate_results(patterns, designs):
    possible_designs_count = 0
    total_arrangement_ways = 0

    for design in designs:
        # Check if the design can be constructed
        if can_construct_design(design, patterns):
            possible_designs_count += 1
            # Count the total number of ways to arrange towels for this design
            total_arrangement_ways += count_ways_to_construct(design, patterns)

    return possible_designs_count, total_arrangement_ways


def read_input_from_file(filename):
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
    
    # First line contains the towel patterns (comma-separated)
    patterns = [pattern.strip() for pattern in lines[0].split(",")]
    
    # Remaining lines are the desired designs
    designs = lines[2:]  # Skip the blank line after patterns
    return patterns, designs


# Main execution
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file name
    patterns_list, designs_list = read_input_from_file(input_file)
    possible_count, total_ways = calculate_results(patterns_list, designs_list)
    print(f"Number of possible designs: {possible_count}")
    print(f"Total number of ways to arrange towels: {total_ways}")
