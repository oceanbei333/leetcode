#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre_head = ListNode(None, head)
        pre = pre_head
        while pre.next and pre.next.next:
            node, succ = pre.next, pre.next.next
            node.next, succ.next = succ.next, node
            pre.next = succ
            pre = node
        return pre_head.next

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head

# @lc code=end
