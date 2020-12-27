#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode()
        plus = 0
        while l1 and l2:
            val = l1.val + l2.val + plus
            p.next = ListNode(val % 10)
            plus = val//10
            l1, l2, p = l1.next, l2.next, p.next
        l3 = l1 or l2
        while l3:
            val = l3.val + plus
            p.next = ListNode(val % 10)
            plus = val//10
            l3, p = l3.next, p.next
        if plus:
            p.next = ListNode(plus)
        return head.next


# @lc code=end
