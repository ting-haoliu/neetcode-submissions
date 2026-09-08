## 📌 Trie (Prefix Tree) – Main Points Template

---

### 1. **What is a Trie?**
- A **tree data structure** used to store words by their **prefixes**.
- Also called a **prefix tree**.
- Each node represents a **single character**.
- Edges connect characters in sequence.

---

### 2. **Why Use a Trie?**
- Fast prefix-based searching.
- Used in **autocomplete**, **spell checkers**, and **dictionary systems**.
- More efficient than brute-force or hashmap for prefix queries.

---

### 3. **Time Complexities**
| Operation       | Time Complexity |
|----------------|------------------|
| Insert Word     | **O(w)**         |
| Search Word     | **O(w)**         |
| Search Prefix   | **O(w)**         |
| Brute-force     | **O(n × m)**     |

> `w` = length of the word  
> `n` = number of words  
> `m` = average word length

---

### 4. **Trie Structure**
- **Root node**: empty, no character.
- Each **TrieNode** contains:
  - `children`: dictionary (character → child node)
  - `word`: boolean (True if a word ends here)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
```

---

### 5. **Main Operations**

#### ✅ Insert
- Traverse each character.
- If missing, create a new node.
- Mark the last node as a word.

```python
def insert(self, word):
    curr = self.root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
    curr.word = True
```

---

#### ✅ Search (exact word)
- Traverse each character.
- Return `False` if a character is missing.
- Return `True` only if the last node has `word = True`.

```python
def search(self, word):
    curr = self.root
    for c in word:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return curr.word
```

---

#### ✅ Starts With (prefix search)
- Traverse each character.
- Return `False` if a character is missing.
- Return `True` if the full prefix exists (no need for `word = True`).

```python
def startsWith(self, prefix):
    curr = self.root
    for c in prefix:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return True
```

---

### 6. **Trie vs Hashmap**
| Feature         | Trie | Hashmap |
|----------------|------|---------|
| Exact match    | ✅   | ✅      |
| Prefix search  | ✅   | ❌      |
| Time per op    | O(w) | O(1) avg |
| Prefix query   | O(w) | O(n) worst |

---

### 7. **Real-World Application**
- **Autocomplete**: suggests words based on typed prefix.
- Efficient because prefix search is **O(w)** and independent of total word count.
