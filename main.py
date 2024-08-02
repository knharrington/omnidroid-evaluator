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
    # use _ since the variable is not used within the loop body
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
def num_sprockets(part):
    # base case - already computed part
    if memotable[part] != -1:
        return memotable[part]
    # base case - part not required by any other part
    if part not in required:
        memotable[part] = sprockets[part]
        return memotable[part]
    # recursize case - calculate total sprokets for part
    memotable[part] = sprockets[part] + sum(num_sprockets(subpart) for subpart in required[part])
    return memotable[part]

# calculate total number of sprockets required
#print("\nCalculating total sprockets")
total_sprockets = num_sprockets(n-1)

# print results
print("\nThe total number of sprockets is in 'output.txt':", total_sprockets)

# write results to output file
with open("output.txt", "w") as out:
    out.write(str(total_sprockets))
