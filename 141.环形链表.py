#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        aset = set()
        while head and id(head) not in aset:
            aset.add(id(head))
            head = head.next
        return bool(head)




# @lc code=end
