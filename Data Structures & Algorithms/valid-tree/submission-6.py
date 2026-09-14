class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # Cycle Detected

        if self.rank[rootX] < self.rank[rootY]:
            self.parents[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parents[rootY] = rootX
        else:
            self.parents[rootY] = rootX
            self.rank[rootX] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Union Find
        # T: O(n∗α(n))
        # S: O(n)
        '''
        1. All nodes should be connected
        2. No cycle
        3. Should have (n - 1) edges
        '''
        if len(edges) != (n - 1):
            return False
        
        uf = UnionFind(n)

        for x, y in edges:
            if not uf.union(x, y):
                return False
        return True
