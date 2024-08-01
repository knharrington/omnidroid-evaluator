# COT 5407 Dynamic Programming Project

Due August 1, 2024

Katie Harrington

Chandan Reddy

Raul Garcia

1. How you can break down a problem instance of the omnidroid construction problem into one or more smaller instances? You may use sprocket[t] to represent the number of sprockets used for part t, and you may use req[t] and use[t] to represent the collection of all parts required to build part t and all parts that part t is used to build, respectively. Your answer should include how the solution to the original problem is constructed from the subproblems.

The parts required to build each part "t" can be represented by req[t]. We need to calculate the total number of sprockets that will be required to build all parts plus the number of sprockets required for part t itself. For example, if part t requires parts x, y, and z, then the problem has to be further broken down for x y and z. Therefore, the total number of sprockets that would be needed for part t is just the sum of the sprockets needed for each part plus sprockets for part t. Every part has it's own sprockets and adding this to the number of sprockets of its dependencies gives total number of sprockets.

2. What is the base case of the omnidroid construction problem?

The base case, or the simplest instance of the problem, is when a part does not require any other parts to be constructed. The total number of sprockets required for that part would only be the number of sprockets specified for that part. 

3. What data structure would you use to recognize repeated problems for omnidroids? You should describe both the abstract data structure, as well as its implementation.

To recognize repeated problems for omnidroids, it would be best to use a dictionary (hash table) in order to perform lookups, insertions, and deletions quickly. A hash table maps keys to values and uses a hash function to compute an index into an array of slots where the desired value can be found.

4. Give pseudocode for a memoized dynamic programming algorithm to calculate the sprockets needed to construct an omnidroid.



5. What is the worst-case time complexity of your memoized algorithm?

The worst case time complexity is O(n) where n represents the number of parts. Each part is only processed once, including its dependencies. The output would be stored in a dictionary or list to avoid recalculation.
