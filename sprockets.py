import sys
from collections import defaultdict

# Function to read the input from a file
def read_input(file_path):
    with open(file_path, "r") as f:
        # Read the number of parts (n) and dependencies (m)
        n, m = map(int, f.readline().split())
        dependencies = []
        # Read each dependency and store it in a list
        for _ in range(m):
            i, j = map(int, f.readline().split())
            dependencies.append((i, j))
        sprockets = []
        # Read the number of sprockets required for each part and store in a list
        for _ in range(n):
            sprockets.append(int(f.readline().strip()))
    return n, m, dependencies, sprockets

# Function to calculate the total number of sprockets needed
def calculate_total_sprockets(n, dependencies, sprockets):
    required = defaultdict(list)
    # Build the dependency list for each part
    for i, j in dependencies:
        required[j].append(i)

    # Memoization table to store results of subproblems
    dp = [-1] * n

    # Helper function to compute sprockets needed for a part
    def dp_calculate(part):
        # If already calculated, return the stored result
        if dp[part] != -1:
            return dp[part]
        # If the part has no dependencies, use its own sprocket count
        if part not in required:
            dp[part] = sprockets[part]
            return dp[part]
        # Calculate total sprockets needed for the part and its dependencies
        dp[part] = sprockets[part] + sum(dp_calculate(subpart) for subpart in required[part])
        return dp[part]

    # Calculate the total sprockets needed for the final part
    total_sprockets = dp_calculate(n - 1)
    return total_sprockets

# Function to write the output to a file
def write_output(file_path, result):
    with open(file_path, "w") as out:
        out.write(str(result))

# Main function to tie everything together
def main(input_file_path, output_file_path):
    # Read input data from the file
    n, m, dependencies, sprockets = read_input(input_file_path)
    # Calculate total sprockets required
    total_sprockets = calculate_total_sprockets(n, dependencies, sprockets)
    # Write the result to the output file
    write_output(output_file_path, total_sprockets)
    print("The total number of sprockets is:", total_sprockets)

# Define input and output file paths
input_file_path = "input.txt"

output_file_path = "output.txt"

# Execute the main function
main(input_file_path, output_file_path)
