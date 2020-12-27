#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        from collections import defaultdict
        count = defaultdict(int)
        node = head
        while node:
            count[node.val] += 1
            node = node.next
        new_head = pre = ListNode()
        node = pre.next = head
        while node:
            if count[node.val] == 1:
                pre = node
            else:
                pre.next = node.next
            node = node.next
        return new_head.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = pre = ListNode()
        pre.next = node = head
        while node and node.next:
            if pre.next.val != node.next.val:
                pre = pre.next
            else:
                while node and node.next and pre.next.val == node.next.val:
                    node = node.next
                pre.next = node.next
            node = node.next
        return new_head.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = pre = ListNode()
        pre.next = cur = head
        while cur and cur.next:
            next_ = cur.next
            if cur.val != next_.val:
                # pre cur  next 各不相同的cur才能成为pre
                pre = cur
            else:
                # 找第一个之前的结点不重复的结点
                while cur and next_ and cur.val == next_.val:
                    cur, next_ = cur.next, next_.next
                pre.next = next_
            cur = cur.next
        return new_head.next
# @lc code=end
