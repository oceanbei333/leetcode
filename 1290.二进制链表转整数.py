#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = '0b'
        while head:
            s+=str(head.val)
            head = head.next
        return int(s, 2)
        
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = res*2+head.val
            head = head.next
        return res
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res <<= 1
            res += head.val
            head = head.next
        return res

# @lc code=end

