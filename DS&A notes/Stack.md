# Summary: Stacks — LIFO Fundamentals, Operations, and Implementations

## 1. What Is a Stack?
A stack is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle: the last element pushed onto the stack is the first one removed.

**Analogy:** A stack of plates — new plates go on top, and you always take the most recently added plate. Removing from the middle isn't allowed; everything above must come off first.

**Real-world uses:**
- Expression evaluation in compilers
- Undo/redo in text editors
- The function call stack in programming languages
- Iterative DFS and backtracking algorithms

## 2. Common Stack Operations (All O(1))

| Operation | Description | Complexity |
|---|---|---|
| **Push** | Adds a new element to the top | **O(1)** |
| **Pop** | Removes and returns the topmost element | **O(1)** |
| **Peek / Top** | Returns the top value without removing it | **O(1)** |
| **IsEmpty** | Checks whether the stack has any elements | **O(1)** |

The constant-time nature of all four operations is what makes stacks efficient.

## 3. Stack Implementations

### Implementation 1: Using Arrays
Maintain an array plus a `top` pointer (initially `-1` for an empty stack). All operations happen at the **end** of the array.

```python
class ArrayStack:
    def __init__(self, size: int):
        self.stack = [0] * size
        self.top = -1
        self.capacity = size

    def push(self, value: int) -> None:
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self) -> int:
        if self.top == -1:
            print("Stack Underflow")
            return -1
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self) -> int:
        if self.top == -1:
            print("Stack is Empty")
            return -1
        return self.stack[self.top]

    def isEmpty(self) -> bool:
        return self.top == -1
```

**How it works:**
- **Push:** Check for room → increment `top` → place value at new top index
- **Pop:** Check if empty → return `stack[top]` → decrement `top`
- **Peek:** Return `stack[top]` without changing `top`
- **IsEmpty:** Check if `top == -1`

**Limitation:** Fixed size — once full, no more pushes unless manually resized. This is why dynamic arrays (`ArrayList` in Java, `list` in Python) are often preferred.

### Implementation 2: Using Linked Lists
The **head** of the linked list represents the **top** of the stack.

```python
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, value: int) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self) -> int:
        if self.head is None:
            print("Stack Underflow")
            return -1
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self) -> int:
        if self.head is None:
            return -1
        return self.head.value

    def isEmpty(self) -> bool:
        return self.head is None
```

**How it works:**
- **Push:** Create a new node → point its `next` to current head → update `head` to the new node
- **Pop:** Check if head is null → return `head.value` → move `head` to `head.next`
- **Peek:** Return `head.value` without removing it
- **IsEmpty:** Check if `head is None`

**Trade-off:** Dynamic size (no resizing needed), but each node stores an extra `next` pointer → **more memory** than a plain array.

### Implementation 3: Built-in Libraries
Most languages provide a tested stack implementation. In Python, use a **list**:

```python
stack = []
stack.append(10)   # Push
stack.append(20)
stack.pop()        # Removes 20
stack[-1]          # Peek (returns 10)
```

- `append()` → **amortized O(1)** (occasional resizes cost O(n) but average out)
- `pop()` from the end → **O(1)**

Unless explicitly asked to implement a stack from scratch, the standard library is the right starting point.

## 4. Key Takeaways
- Stacks follow **LIFO** — last in, first out.
- All four core operations (**push, pop, peek, isEmpty**) run in **O(1)** time.
- **Array-based** stacks are simple but fixed-size; **linked-list** stacks are dynamic but use extra memory per node.
- Python's `list` (with `append`/`pop`) is the idiomatic stack for most use cases.


# Summary: Monotonic Stack — O(n) Next/Previous Greater/Smaller Patterns

## 1. What Is a Monotonic Stack?
A **Monotonic Stack** is a stack whose elements stay in either **increasing or decreasing order** from bottom to top. Before pushing a new element, you **pop all stack-top elements that violate the invariant**.

- **Monotonic Increasing Stack:** values from bottom to top increase. Before pushing, pop top elements that violate the order. Example: `2 → 5 → 8`, next must be greater than 8.
- **Monotonic Decreasing Stack:** values from bottom to top decrease. Example: `9 → 6 → 4`, next must be smaller than 4.

**Key practice:** Store **indices** rather than values — this gives access to both position and value (`nums[stack[-1]]`), which is needed for distance/width calculations.

**Strict vs Non-Strict:** The comparison (`>` vs `>=`) determines what happens to equal elements:
- **Strict (`>`):** equal elements stay on the stack and become part of the answer chain (e.g., Daily Temperatures).
- **Non-strict (`>=`):** equal elements pop each other and are merged (e.g., Largest Rectangle in Histogram).

## 2. Example Problem: Next Greater Element

**Task:** For each number, find the first number to its right that is larger.

Array: `[2, 1, 5, 6, 2, 3]` → Result: `[5, 5, 6, -1, 3, -1]`

### Brute Force — O(n²)
```python
class Solution:
    def nextGreaterElementBruteForce(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = -1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    result[i] = nums[j]
                    break
        return result
```

### Monotonic Stack — O(n)
```python
class Solution:
    def nextGreaterElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n  # Initialize all results to -1
        stack = []  # Store indices

        for i in range(n):
            # While stack not empty AND current element is greater
            # than element at index stored at top of stack
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]  # Found next greater element

            stack.append(i)

        # Remaining indices have no next greater element (already -1)
        return result
```

### Step-by-Step Walkthrough

| Index | Value | Action | Stack (indices) | Result |
|---|---|---|---|---|
| 0 | 2 | push | [0] | [-1,-1,-1,-1,-1,-1] |
| 1 | 1 | 1 < 2, push | [0,1] | [-1,-1,-1,-1,-1,-1] |
| 2 | 5 | pop 1 (result[1]=5), pop 0 (result[0]=5), push 2 | [2] | [5,5,-1,-1,-1,-1] |
| 3 | 6 | pop 2 (result[2]=6), push 3 | [3] | [5,5,6,-1,-1,-1] |
| 4 | 2 | 2 < 6, push | [3,4] | [5,5,6,-1,-1,-1] |
| 5 | 3 | pop 4 (result[4]=3), push 5 | [3,5] | [5,5,6,-1,3,-1] |

Final result: `[5, 5, 6, -1, 3, -1]`

## 3. Why It's O(n) Despite the Nested While Loop
**Amortized analysis:** Each index is **pushed exactly once** and **popped at most once**. Total pushes = n, total pops ≤ n. The inner while loop's cost across the entire outer loop sums to at most n (not n per iteration). Combined work: n pushes + n pops + n outer iterations = **O(n)**.

## 4. Four Canonical Variants

| Goal | Traversal | Stack Order | When to Pop |
|---|---|---|---|
| **Next Greater** (right) | left → right | decreasing | pop while top < current |
| **Previous Greater** (left) | left → right | decreasing | pop while top <= current; answer = new top before push |
| **Next Smaller** (right) | left → right | increasing | pop while top > current |
| **Previous Smaller** (left) | left → right | increasing | pop while top >= current; answer = new top before push |

- **"Right" variants:** record the answer at the moment of popping (the element that triggers the pop is the next greater/smaller for the popped index).
- **"Left" variants:** record the answer from the stack top **before** pushing the current index.

### Previous Smaller Element Template
```python
class Solution:
    def previousSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n):
            # Pop everything that is not strictly smaller than current
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            # Whatever survives on top is the previous smaller index
            if stack:
                result[i] = stack[-1]

            stack.append(i)

        return result
```

## 5. The Sentinel Trick
For problems like **Largest Rectangle in Histogram** or **Sum of Subarray Minimums**, every remaining element must be processed when the loop ends. Append a **sentinel value** that forces all remaining elements to pop:
- Histogram problems → append `0` (smaller than any bar)
- Next-greater problems → append `INT_MAX` (larger than any value)

```java
// Largest Rectangle in Histogram with sentinel
int[] withSentinel = Arrays.copyOf(heights, heights.length + 1);
withSentinel[heights.length] = 0;  // forces all bars to pop
// ... single loop, no post-processing needed
```

This removes the need to duplicate the loop body after the main loop to drain the stack.

## 6. Monotonic Stack vs Monotonic Deque

| | Monotonic Stack | Monotonic Deque |
|---|---|---|
| Structure | LIFO | Double-ended queue |
| Use case | Next/previous greater/smaller | Sliding window constraints |
| Front eviction | Never | Yes, when index falls outside window |
| Back mechanics | Identical (pop to maintain invariant) | Identical |

**Canonical deque example:** Sliding Window Maximum (LC 239) — deque holds candidate indices in decreasing value order; front is the current window's max; elements are evicted from the front when out of window bounds.

> A monotonic stack is what a monotonic deque becomes when no front-side eviction is ever needed.

## 7. Classic Problems

| Problem | Pattern |
|---|---|
| **Daily Temperatures** (LC 739) | Next-greater-right; record `j - i` (index distance) when popping |
| **Largest Rectangle in Histogram** (LC 84) | Previous-smaller + next-smaller boundaries determine width |
| **Trapping Rain Water** (LC 42) | Decreasing stack; each pop = a valley, water computed from popped height + boundaries |
| **Sum of Subarray Minimums** (LC 907) | Previous-smaller-or-equal + next-smaller; count subarrays per element |
| **Stock Span** (LC 901) | Previous-greater; answer = index distances |
| **Next Greater Element II** (LC 503) | Circular array; iterate twice or use `i % n` |

## 8. Why Store Indices Instead of Values
Storing indices keeps **positional information** available:
- Daily Temperatures needs `j - i` (days between)
- Largest Rectangle needs boundary index (width) and bar height (area)

**Default:** Store indices, compare via `nums[stack[-1]]`. The index gives both position and value; the reverse is not true.

## 9. Key Takeaways
- Monotonic stacks reduce many array problems from **O(n²) to O(n)**.
- The stack maintains an **increasing or decreasing invariant** by popping violating elements before pushing.
- **Strict vs non-strict comparison** controls how equal elements are treated — choose based on the problem.
- **Store indices**, not values, for maximum flexibility.
- Four variants (next/previous × greater/smaller) are obtained by flipping comparison and recording timing.
- The **sentinel trick** eliminates post-loop cleanup.
- Use a **monotonic deque** instead when sliding-window front eviction is needed.
