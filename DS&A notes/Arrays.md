# Summary: Arrays — Fundamentals, Operations, and Interview Patterns

## 1. What Is an Array?
An array is a data structure that stores a collection of elements **of the same type** in a **contiguous block of memory**. Elements are accessed via an **index**, and most languages use **zero-based indexing** (first element at index 0).

**Why access is fast:** Because elements sit next to each other, the address of any element can be computed directly:

```
address of arr[i] = base address + (i × size of each element)
```

This gives **O(1)** random access regardless of array size.

**Limitation:** In languages like C++ and Java, arrays have a **fixed size**. To grow, you must allocate a new larger array and copy data over — **O(n)** time.

## 2. Dynamic Arrays
Most languages provide resizable arrays:
- Python → `list`
- Java → `ArrayList`
- C++ → `vector`

Internally they **over-allocate** memory. When capacity runs out, they typically **double** the capacity and copy all elements (**O(n)**). Because this is rare, appending at the end is **amortized O(1)**.

## 3. Common Array Operations & Complexities

| Operation | Complexity | Notes |
|---|---|---|
| Access by index | **O(1)** | Direct address calculation |
| Traversal | **O(n)** | Visit each element once |
| Insert at end | **Amortized O(1)** | Occasional resize costs O(n) |
| Insert at beginning/middle | **O(n)** | Must shift elements right |
| Delete last | **O(1)** | No shifting |
| Delete first/middle | **O(n)** | Must shift elements left |
| Search (unsorted) | **O(n)** | Linear scan |
| Search (sorted) | **O(log n)** | Binary search |

### Code Examples

**Access by index:**
```python
class ArrayAccessExample:
    @staticmethod
    def main():
        arr = [10, 20, 30, 40, 50]
        index = 2
        value = arr[index]
        print(f"Element at index {index} = {value}")

if __name__ == "__main__":
    ArrayAccessExample.main()
```

**Traversal:**
```python
class ArrayTraversalExample:
    @staticmethod
    def main():
        arr = [3, 5, 7, 9, 11]
        print("Array elements: ", end="")
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()

if __name__ == "__main__":
    ArrayTraversalExample.main()
```

## 4. Common Array Interview Patterns

### Pattern 1: Two Pointer Technique
Works on **sorted arrays**. One pointer starts at the left, one at the right; they move toward each other based on a comparison. Reduces O(n²) brute force to **O(n)** time and **O(1)** space.

**Use cases:** Two Sum on sorted array, 3Sum, 4Sum, removing duplicates in place, palindrome check, merging sorted arrays.

```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1        # need a larger value
        else:
            right -= 1       # need a smaller value
    return [-1, -1]
```
For `nums = [1, 3, 5, 7, 9, 11]`, `target = 12` → returns `[0, 5]` (1 + 11).

### Pattern 2: Sliding Window
For problems about a **contiguous subarray or substring**. Maintain a window that moves across the array, updating the property incrementally (one element enters, one leaves → O(1) per shift). Whole scan is **O(n)**.

**Two flavors:**
- **Fixed-size** window (width given)
- **Variable-size** window (grows/shrinks based on a condition, e.g., longest substring without repeating characters)

```python
def max_sum_window(nums, k):
    window = sum(nums[:k])             # first window
    max_sum = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]  # slide by one
        max_sum = max(max_sum, window)
    return max_sum
```
For `nums = [1, 3, 5, 7, 9, 11]`, `k = 3` → max sum is **27** (`[7, 9, 11]`).

### Pattern 3: Prefix Sum
`prefix[i]` = sum of `nums[0..i]`. Once built, any range sum `[L, R]` is `prefix[R] − prefix[L−1]` (or `prefix[R]` if `L == 0`). Construction: **O(n)** time/space; each query: **O(1)**.

**Extensions:** prefix XOR, prefix counts, 2D prefix sums.

```python
class RangeSum:
    def __init__(self, nums):
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def query(self, l, r):
        if l == 0:
            return self.prefix[r]
        return self.prefix[r] - self.prefix[l - 1]
```

### Pattern 4: Dynamic Programming with Arrays
Use a 1D or 2D array (DP table) to cache solutions to subproblems.

**Recipe:**
1. Identify what each cell represents
2. Write a recurrence in terms of earlier cells
3. Define base cases
4. Fill in dependency-safe order

**Example — Climbing Stairs:** `ways[i] = ways[i−1] + ways[i−2]`, `ways[0] = ways[1] = 1` (Fibonacci in disguise).

```python
def climb_stairs(n):
    if n <= 1:
        return 1
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
```
For `n = 5` → table `[1, 1, 2, 3, 5, 8]` → **8 ways**. O(n) time, O(n) space (reducible to O(1)).

**Common DP problems:** House Robber, Coin Change, Longest Increasing Subsequence, 0/1 Knapsack.

## 5. Key Takeaway
Arrays are the foundation for many data structures and algorithms. Mastering the four core patterns — **two pointers, sliding window, prefix sum, and dynamic programming** — transforms arrays from a simple storage container into a powerful algorithmic tool.
