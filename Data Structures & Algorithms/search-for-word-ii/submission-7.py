class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie
        # T: O(n * m * 4^L)
        # S: O(W * L + n * m)

        # Build Trie
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        # DFS
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []

        def dfs(r: int, c: int, node: Optional['TrieNode']) -> None:
            # Check bounds and if cell already visited
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if board[r][c] == '#':
                return
            
            char = board[r][c]
            if char not in node.children:
                return


            next_node = node.children[char]
            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None

            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, next_node)
            
            board[r][c] = char


        root = trie.root
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res
