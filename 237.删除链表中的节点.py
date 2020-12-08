#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        first = node
        second = first.next
        third = second.next
        first.val = second.val
        while third:
            first , second, third = first.next, second.next, third.next
            first.val = second.val
        first.next = None
    def deleteNode(self, node):
        pre = node
        node = node.next
        pre.val = node.val
        while node.next:
            pre, node = pre.next, node.next
            pre.val = node.val
        pre.next = None
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


        
# @lc code=end

