# Summary: Topological Sort

## What It Is

Topological sort produces a **linear ordering of vertices** in a **Directed Acyclic Graph (DAG)** such that for every edge `u → v`, vertex `u` appears before vertex `v`. It answers: *"In what order should I process elements when some depend on others?"*

**Key properties:**
- Works **only on DAGs** — a cycle makes a valid ordering impossible (circular dependency).
- Multiple valid orderings may exist for the same graph.
- Works on **disconnected graphs** too — the order between independent components doesn't matter.

**Real-world uses:** course prerequisites, task scheduling, compilers (function/module dependencies), package managers (npm, pip).

---

## Two Implementation Methods

### Method 1: DFS (Recursive, Post-Order)

**Idea:** Explore each path to its deepest point. Push a node onto a stack **after** all its neighbors are visited (during backtracking). Reverse the result (or pop the stack) to get the topological order.

```python
class TopologicalSortDFS:
    @staticmethod
    def dfs(node, adj, visited, stack):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                TopologicalSortDFS.dfs(neighbor, adj, visited, stack)
        stack.append(node)  # push after all dependencies visited

    @staticmethod
    def topologicalSort(V, adj):
        stack = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                TopologicalSortDFS.dfs(i, adj, visited, stack)
        topoOrder = []
        while stack:
            topoOrder.append(stack.pop())
        return topoOrder
```

**Simpler variant** (reverse at the end instead of using a stack):

```python
def topologicalSort(edges, n):
    adj = {i: [] for i in range(1, n + 1)}
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    visit = set()
    for i in range(1, n + 1):
        dfs(i, adj, visit, topSort)
    topSort.reverse()
    return topSort

def dfs(src, adj, visit, topSort):
    if src in visit:
        return
    visit.add(src)
    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)
```

**Cycle detection (DFS):** Add a `path` set tracking the current DFS path. If a vertex is revisited along the same path, a cycle exists.

---

### Method 2: Kahn's Algorithm (BFS, Iterative)

**Idea:** Repeatedly remove nodes with **in-degree 0** (no unmet dependencies). When a node is removed, decrement its neighbors' in-degrees; any neighbor reaching 0 becomes ready.

**Steps:**
1. Compute in-degree for every node.
2. Enqueue all nodes with in-degree 0.
3. While queue is non-empty: dequeue a node, add to result, decrement neighbors' in-degrees, enqueue any that hit 0.
4. If result has fewer than `V` nodes → **cycle detected**.

```python
class TopologicalSortBFS:
    @staticmethod
    def topologicalSort(V, adj):
        indegree = [0] * V
        for neighbors in adj:
            for neighbor in neighbors:
                indegree[neighbor] += 1

        queue = [i for i in range(V) if indegree[i] == 0]
        topoOrder = []
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            topoOrder.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return topoOrder
```

---

## Complexity

| Aspect | DFS | Kahn's (BFS) |
|---|---|---|
| **Time** | O(V + E) | O(V + E) |
| **Space (auxiliary)** | O(V) | O(V) |
| **Style** | Recursive (stack depth risk on deep graphs) | Iterative (no recursion limit) |
| **Cycle detection** | Needs extra `path`/color array | Automatic (result < V) |

---

## Key Takeaways

- Topological sort orders a DAG so every edge `u → v` has `u` before `v`.
- Only valid on **acyclic** graphs; cycles make ordering impossible.
- **DFS approach:** push nodes after exploring neighbors, then reverse.
- **Kahn's approach:** repeatedly emit in-degree-0 nodes, decrementing neighbors.
- Both run in **O(V + E)** time and **O(V)** auxiliary space.
- A graph can have **multiple valid topological orderings**.
