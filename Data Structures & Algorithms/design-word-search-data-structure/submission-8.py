class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # T: O(n)
    # S: O(n)
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    # T: O(n)
    # S: O(1)
    def search(self, word: str) -> bool:
        # DFS
        def dfs(index: int, node: Optional['TrieNode']) -> bool:
            if index == len(word):
                return node.isEnd

            c = word[index]

            # 1. c is "."
            if c == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            # 2. c is not "."
            else:
                if c not in node.children:
                    return False
                return dfs(index + 1, node.children[c])
        
        return dfs(0, self.root)
