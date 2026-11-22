# Binary Search Cheat Sheet

## 1. What It Is

Binary search finds an answer in a **sorted search space** by halving the range each step.

| Method | Time |
|---|---|
| Linear Search | O(n) |
| Binary Search | O(log n) |

**Core idea:** each step, one side is *definitely not* the answer. Keep shrinking the "possible answer" range.

Example: `nums = [1,3,5,7,9,11,13]`, `target = 9`
`mid=7` → go right → `mid=11` → go left → `mid=9` → found.

---

## 2. Exact Match (LeetCode 704)

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Why `left <= right`?** When `left == right`, one candidate remains and still needs checking.

---

## 3. Boundary Search (Most Common in Interviews)

Typical tasks: first/last occurrence, first/last True, minimum/maximum valid value.

### Lower Bound (first index ≥ target)

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid          # mid might be the answer, don't discard it
    return left
```

`[1,2,2,2,3,4]`, target 2 → `1`

### Upper Bound (first index > target)

```python
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
```

`[1,2,2,2,3]`, target 2 → `4`

---

## 4. Binary Search on Answer

Instead of searching an array, search the **space of possible answers** by defining `check(x)` — "is `x` feasible?"

**Keywords:** minimum speed / capacity / days, maximum distance, smallest/largest valid value.

**Example: Koko Eating Bananas (LC 875)**
`piles = [3,6,7,11]`, `h = 8` → find the minimum eating speed.

`can_finish(speed)` yields `F F F T T T` for speeds 1–6. This **monotonic** pattern is the signal for binary search.

```python
left, right = 1, max(piles)
while left < right:
    mid = (left + right) // 2
    if can_finish(mid):
        right = mid
    else:
        left = mid + 1
return left
```

---

## 5. How to Recognize a Binary Search Problem

1. Is the search space ordered (array index, or range of possible answers)?
2. Can you define `check(x)` so results look like `F F F T T T` or `T T T F F F`?

If yes to both → binary search (on answer).

---

## 6. Three Templates to Memorize

### A. Exact Match
Use for: LC 704, general lookup.

```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid + 1
    else: right = mid - 1
```

### B. First True (`F F F T T T`)
Use for: lower bound, Koko Eating Bananas, Capacity to Ship Packages.

```python
while left < right:
    mid = (left + right) // 2
    if check(mid): right = mid
    else: left = mid + 1
return left
```

### C. Last True (`T T T F F F`)

```python
while left < right:
    mid = (left + right + 1) // 2   # the +1 avoids an infinite loop
    if check(mid): left = mid
    else: right = mid - 1
return left
```

> **Remember:** when using `left = mid`, always round `mid` up (`+ 1`).
