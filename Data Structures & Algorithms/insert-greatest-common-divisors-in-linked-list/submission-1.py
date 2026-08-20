# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(n)
        # S: O(1)
        curr = head

        while curr and curr.next:
            gcd = self._gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        return head
    
    def _gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b , a % b
        
        return a