# COT 5407 Dynamic Programming Project

Katie Harrington

Chandan Reddy

Raul Garcia

**1. How you can break down a problem instance of the omnidroid construction problem into one or more smaller instances? You may use sprocket[t] to represent the number of sprockets used for part t, and you may use req[t] and use[t] to represent the collection of all parts required to build part t and all parts that part t is used to build, respectively. Your answer should include how the solution to the original problem is constructed from the subproblems.**

The omnidroid problem can be broken down into smaller instances by determining the total number of sprockets for each part, *t*, specifically by considering both the sprockets needed for part *t* and the ones needed for its dependencies. The parts required to build each part *t* can be represented by req[*t*]. To calculate the total number of sprockets that will be required to build part *t*, we can recursively calculate the number of sprockets for each part in req[*t*]: total_sprockets(*t*)=sprocket[*t*]+∑(subpart∈req[*t*]) * total_sprockets(subpart).

For example, if part *t* requires parts *x*, *y*, and *z*, then the problem has to be further broken down for *x*, *y*, and *z*. Therefore, the total number of sprockets that would be needed for part *t* is the sum of the sprockets needed for each subpart plus sprockets for part *t*. Every part has it's own sprocket cost and adding these costs to the number of sprockets of its dependencies gives the total number of sprockets.

**2. What is the base case of the omnidroid construction problem?**

The base case, or the simplest instance of the problem, is when a part does not require any other parts to be constructed. The total number of sprockets required for that part would only be the number of sprockets specified for that part. 

**3. What data structure would you use to recognize repeated problems for omnidroids? You should describe both the abstract data structure, as well as its implementation.**

To recognize repeated problems for omnidroids, it would be best to use a dictionary in order to perform lookups, insertions, and deletions quickly. This dictionary is implemented in the form of a memoization table that stores the results of subproblems to avoid redundant calculations. Each index *i* of the list represents a part, and the value at that index stores the number of sprockets required for that part.

**4. Give pseudocode for a memoized dynamic programming algorithm to calculate the sprockets needed to construct an omnidroid.**

```
initialize memotable with -1 for each part

function calculate_sprockets(part):
    if memotable[part] != -1:
        return memotable[part]
    
    if part not in required:
        memotable[part] = sprockets[part]
        return memotable[part]
    
    total_sprockets = sprockets[part]
    for subpart in required[part]:
        total_sprockets += calculate_sprockets(subpart)
    
    memotable[part] = total_sprockets
    return memotable[part]

total_sprockets = calculate_sprockets(final_part)
```

**5. What is the worst-case time complexity of your memoized algorithm?**

The worst case time complexity is O(*n*) where *n* represents the number of parts. Initializing the memoization table to avoid recalculation takes O(*n*) time. Each part is only processed once, including its dependencies, *m*, which takes O(*n* + *m*) time. Therefore the overall time complexity is O(*n*).
