#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aset = set()
        while headA:
            aset.add(headA)
            headA = headA.next
        while headB:
            if headB in aset:
                return headB
            headB = headB.next
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeB
            if nodeA.next:
                nodeA = nodeA.next
            else:
                nodeA = headB
                headB = None
            if nodeB.next:
                nodeB = nodeB.next
            else:
                nodeB = headA
                headA = None



# @lc code=end

