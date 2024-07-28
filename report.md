# COT 5407 Dynamic Programming Project

Due August 1, 2024

Katie Harrington

Chandan Reddy

Raul Garcia

1. How you can break down a problem instance of the omnidroid construction problem into one or more smaller instances? You may use sprocket[t] to represent the number of sprockets used for part t, and you may use req[t] and use[t] to represent the collection of all parts required to build part t and all parts that part t is used to build, respectively. Your answer should include how the solution to the original problem is constructed from the subproblems.



2. What is the base case of the omnidroid construction problem?

The base case, or the simplest instance of the problem, is when a part does not require any other parts to be constructed. The tota; number of sprockets required for that part would only be the number of sprockets soecified for that part.

3. What data structure would you use to recognize repeated problems for omnidroids? You should describe both the abstract data structure, as well as its implementation.

To recognize repeated problemf for omnidroids, it would be best to use a dictionary (hash table) in order perform lookups, insertions, and deletions quickly. A hash table maps keys to values and uses a hash function to compute an index into an array of slots where the desired value can be found.

4. Give pseudocode for a memoized dynamic programming algorithm to calculate the sprockets needed to construct an omnidroid.



5. What is the worst-case time complexity of your memoized algorithm?
