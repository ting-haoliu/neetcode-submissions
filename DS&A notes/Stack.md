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
