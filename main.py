# COT5402 Dynamic Programming Project

import sys
from collections import defaultdict

# Accept command line arguments - one input file at a time
if len(sys.argv) != 1:
    raise ValueError('Please provide one file name.')

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

print("\nn =", n)
print("\nm =", m)
print("\ndependencies =", dependencies)
print("\nsprockets =", sprockets)
    
# set up data structures
print("\nSetting up data structures")
depend = defaultdict(list)
used = defaultdict(list)

# fill dictionaries based on dependencies
for i, j in dependencies:
    depend[j].append(i)
    used[i].append(j)

# initialize memoization table to store the cost of sprockets
memotable = [-1] * n