# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Slow and fast pointers
        # T: O(n)
        # S: O(1)
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second list
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Calculate max twin sum
        res = 0
        first, second = head, prev
        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next
        
        return res
