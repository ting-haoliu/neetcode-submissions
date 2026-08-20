# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Singly Linked List
        # T: O(n)
        # S: O(1)
        curr = head

        while curr and curr.next:
            new_node = ListNode(math.gcd(curr.val, curr.next.val))
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        return head
