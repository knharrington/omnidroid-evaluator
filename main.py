# COT5402 Dynamic Programming Project

import sys

# Accept command line arguments - one input file at a time
if len(sys.argv) != 1:
    raise ValueError('Please provide one file name.')

inputParts = sys.argv[1]
print("\nThe file that has all the inputs is:", inputParts)

# Open and read text file
with open(inputParts, "r") as f:
    