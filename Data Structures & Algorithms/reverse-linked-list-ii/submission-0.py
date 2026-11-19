# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Singly Linked List
        # T: O(n)
        # S: O(1)
        if left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        
        # Move prev to the node just before the reversal starts
        for _ in range(left - 1):
            prev = prev.next

        # Perform head insertion (right - left) times
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
