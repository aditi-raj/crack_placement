# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        res = 0
        while head:
            res += (2 ** (l - 1)) * head.val
            head = head.next
            l -= 1
        return res
