# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Linked List
        # T: O(n)
        # S: O(1)
        dummy = ListNode(0, head)
        L, R = dummy, head

        while n:
            R = R.next
            n -= 1

        while R:
            L = L.next
            R = R.next
        L.next = L.next.next

        return dummy.next
