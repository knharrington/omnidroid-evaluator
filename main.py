# COT5402 Dynamic Programming Project

import sys
from collections import defaultdict

# accept command line arguments - one input file at a time
if len(sys.argv) != 2:
    raise ValueError('Please provide one file name')

inputParts = sys.argv[1]
print("\nReading input file:", inputParts)

# Open and read text file
with open(inputParts, "r") as f:
    # extract number of parts (n) and number of dependencies (m)
    n, m = map(int, f.readline().split())
    # figure out number of dependencies (m) between parts
    dependencies = []
    for _ in range(m):
        i, j = map(int, f.readline().split())
        dependencies.append((i, j))
    # extract sprockets required for each part
    sprockets = []
    for _ in range(n):
        sprockets.append(int(f.readline().strip()))

print("\nThere are", n, "parts requiring sprockets:", sprockets)
print("\nThere are", m, "dependencies:", dependencies)
    
# set up dictionary
#print("\nSetting up dictionary")
required = defaultdict(list)

# fill dictionary based on dependencies
for i, j in dependencies:
    required[j].append(i)

# initialize memoization table to store the cost of sprockets
memotable = [-1] * n

# define dynammic programming function 
def calculate_sprockets(part):
    if memotable[part] != -1:
        return memotable[part]
    if part not in required:
        memotable[part] = sprockets[part]
        return memotable[part]
    memotable[part] = sprockets[part] + sum(calculate_sprockets(subpart) for subpart in required[part])
    return memotable[part]

# calculate total number of sprockets required
#print("\nCalculating total sprockets")
total_sprockets = calculate_sprockets(n-1)

# print results
print("\nThe total number of sprockets is in 'output.txt':", total_sprockets)

# write results to output file
with open("output.txt", "w") as out:
    out.write(str(total_sprockets))
