## 📌 Union Find (Disjoint Sets) – Main Points Template

---

### 1. **What is Union-Find?**
- A data structure for tracking **connected components** in a graph.
- Used to **detect cycles** in a graph.
- Better than DFS for **dynamic graphs** (edges added over time).
- Operates on **disjoint sets**.

---

### 2. **Disjoint Sets**
- Sets with **no elements in common** (intersection = empty).
- Example:
  - ✅ Disjoint: `S1 = {1,2,3}`, `S2 = {4,5,6}`
  - ❌ Not disjoint: `S3 = {1,2,5}`, `S4 = {5,6,7}`

---

### 3. **Core Concept**
- Union-Find is a **"forest of trees"**.
- Each vertex initially:
  - Is its own parent.
  - Has rank = 0.
- Two key operations:
  - **Find** → finds the root parent of a node.
  - **Union** → connects two components (only if they are disjoint).

---

### 4. **Implementation**

#### ✅ Initial Setup
```python
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
```

---

#### ✅ Find (with Path Compression)
- Traverses up to the root parent.
- **Path compression**: updates parents to point directly to root.

```python
def find(self, n):
    if n != self.par[n]:
        self.par[n] = self.find(self.par[n])
    return self.par[n]
```

---

#### ✅ Union (with Union by Rank)
- If both nodes share the same root → **cycle detected**, return `False`.
- Attach smaller rank tree under larger rank tree.
- If ranks equal → pick one as parent, increment its rank.

```python
def union(self, n1, n2):
    p1, p2 = self.find(n1), self.find(n2)
    if p1 == p2:
        return False

    if self.rank[p1] > self.rank[p2]:
        self.par[p2] = p1
    elif self.rank[p1] < self.rank[p2]:
        self.par[p1] = p2
    else:
        self.par[p1] = p2
        self.rank[p2] += 1
    return True
```

---

### 5. **Cycle Detection Example**
- Edges: `[1,2], [4,1], [2,4]`
  - Union(1,2) → connect 2 → 1
  - Union(4,1) → connect 4 → 1
  - Union(2,4) → same root (1) → **cycle detected**

---

### 6. **Time & Space Complexity**

| Scenario | Time Complexity |
|----------|-----------------|
| Naive find | **O(n)** (worst case: chain) |
| With union by rank + path compression | **O(α(n))** ≈ **O(1)** |
| Total for `m` edges | **O(m × α(n))** ≈ **O(m)** |

> `α(n)` = Inverse Ackermann function (practically constant)

---

### 7. **Key Optimizations**
| Optimization | Purpose |
|--------------|---------|
| **Path Compression** | Flattens tree during `find` |
| **Union by Rank** | Keeps tree height minimal |

---

### 8. **When to Use Union-Find**
- ✅ Dynamic graph connectivity
- ✅ Cycle detection in undirected graphs
- ✅ Kruskal's MST algorithm
- ❌ Static graphs (DFS may be simpler)
