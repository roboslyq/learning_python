# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from com.roboslyq.python.leetcode.listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pre = None
        cur = head
        while cur.next is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        cur.next = pre
        return cur
