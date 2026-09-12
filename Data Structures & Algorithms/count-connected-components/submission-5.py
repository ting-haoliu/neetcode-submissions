class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # already in the same tree

        if self.rank[rootX] > self.rank[rootY]:
            self.parents[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parents[rootX] = rootY
        else:
            self.parents[rootY] = rootX
            self.rank[rootX] += 1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # T: O(n α(n))
        # S: O(n)
        count = n
        uf = UnionFind(n)

        for x, y in edges:
            if uf.union(x, y):
                count -= 1
        
        return count
        