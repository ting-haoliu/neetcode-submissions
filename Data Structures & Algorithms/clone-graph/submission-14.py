"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Adjacency List
        # DFS
        # T: O(V + E)
        # S: O(V)
        if not node:
            return None

        oldToNew = {}

        def dfs(currNode: Optional['Node']) -> Optional['Node']:
            if currNode in oldToNew:
                return oldToNew[currNode]

            copyNode = Node(currNode.val)
            oldToNew[currNode] = copyNode

            for nei in currNode.neighbors:
                copyNode.neighbors.append(dfs(nei))
            
            return copyNode

        return dfs(node)
        