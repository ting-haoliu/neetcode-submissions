"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Linked List
        # T: O(n)
        # S: O(1)
        if not head:
            return None

        # Copy nodes, and put each copys next to the original ones
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next

        # Copy the random nodes
        # A.random -> B => A'.random -> B'
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next

        # Separate two lists
        curr = head
        copyHead = curr.next
        currCopy = copyHead

        while curr:
            curr.next = currCopy.next
            if currCopy.next:
                currCopy.next = currCopy.next.next
            curr = curr.next
            currCopy = currCopy.next
        
        return copyHead
