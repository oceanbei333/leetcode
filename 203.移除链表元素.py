#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        first = pre = ListNode(None)
        pre.next = head
        node = head
        while node:
            if node.val == val:
                pre.next = node.next
            else:
                pre = pre.next
            node = node.next
        return first.next
        
# @lc code=end

