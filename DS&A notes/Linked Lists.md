# Summary: Linked Lists

## What is a Linked List?
A **linear data structure** made of nodes, where each node contains:
- A **value** (the data)
- A **pointer/reference** to the next node

The last node points to `null`. Unlike arrays, nodes are **scattered across memory** (not contiguous), so insertion/deletion doesn't require shifting data, but direct access to an element requires **O(n) traversal** from the head.

---

## Types of Linked Lists

| Type | Structure | Trade-off |
|------|-----------|-----------|
| **Singly** | Each node points to next only | Simple, memory-efficient; no backward traversal |
| **Doubly** | Each node points to next and prev | Bidirectional; extra memory & complexity |
| **Circular** | Last node points back to first | Good for cyclical behavior (round-robin, games) |

### Code Examples

**Singly:**
```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next
```

**Doubly:**
```python
class DoublyListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None
```

**Circular:**
```python
class CircularListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = self  # initially points to itself
```

---

## Operations & Time Complexities

| Operation | Singly | Doubly (with tail) |
|-----------|--------|---------------------|
| Traverse | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at start | O(1) | O(1) |
| Insert at end | O(n) / O(1) with tail | O(1) |
| Insert at index | O(n) | O(n) |
| Delete from start | O(1) | O(1) |
| Delete from end | O(n) | O(1) |
| Delete at index | O(n) | O(n) |

**Key notes:**
- O(1) insert/delete assumes you already have a reference to the node.
- Singly reaches O(1) insert-at-end only with a **tail pointer**.
- "Delete at index" is O(n) because the cost is in **reaching** the index.

### Code Examples

**Traversal:**
```python
current = head
while current is not None:
    print(current.val)
    current = current.next
```

**Search:**
```python
current = head
while current is not None:
    if current.val == target:
        return True
    current = current.next
```

**Insert at beginning:**
```python
newNode.next = head
head = newNode
```

**Delete from beginning:**
```python
head = head.next
```

---

## Common Interview Patterns

### 1. Fast and Slow Pointers (Floyd's Tortoise and Hare)
- Slow moves 1 step; fast moves 2 steps.
- **Find middle:** When fast reaches end, slow is at midpoint.
- **Cycle detection:** If a cycle exists, fast laps slow and they meet.

```python
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
Both run in **O(n) time, O(1) space**.

### 2. In-Place Reversal
Flip every `next` pointer using three pointers: `prev`, `curr`, `next`.

```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # save the rest of the list
        curr.next = prev      # flip the pointer
        prev = curr           # shift prev forward
        curr = nxt            # shift curr forward
    return prev               # prev is the new head
```
**O(n) time, O(1) space.** Used in Reverse Linked List, Palindrome Linked List, Reverse Nodes in k-Group, Reorder List.

### 3. Dummy Nodes
A placeholder before the real head so the head is **never a special case**.

**Without dummy (special case for head):**
```python
def remove_first_match(head, target):
    if head and head.val == target:
        return head.next
    curr = head
    while curr.next and curr.next.val != target:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return head
```

**With dummy (uniform handling):**
```python
def remove_first_match(head, target):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next and curr.next.val != target:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return dummy.next  # dummy.next is the (possibly new) head
```
Useful for operations that may modify the head: insertion at front, merging sorted lists, removing nth from end, removing duplicates, partitioning.

---

## Key Takeaways
- Linked lists offer **dynamic sizing** and **O(1) insert/delete** (with reference) but **O(n) access**.
- Choose singly, doubly, or circular based on traversal needs.
- Master the three patterns: **fast/slow pointers**, **in-place reversal**, and **dummy nodes** — they cover most interview questions.
