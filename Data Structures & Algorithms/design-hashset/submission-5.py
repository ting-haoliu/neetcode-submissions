class MyHashSet:
    # Array
    # T: O(1)
    # S: O(k)
    
    def __init__(self):
        self.mySet = [False] * 1000001

    def add(self, key: int) -> None:
        self.mySet[key] = True

    def remove(self, key: int) -> None:
        self.mySet[key] = False

    def contains(self, key: int) -> bool:
        return self.mySet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)