#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, length):
        pre = None
        for _ in range(length):
            temp = head.next
            head.next = pre
            pre = head
            head= temp
        return pre, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        tail = hair = ListNode(None, head)
        for _ in range(length//k):
            new_head, next_head = self.reverse(head, k)
            tail.next = new_head
            tail = head
            head = next_head
        if length%k:
            tail.next = next_head
        return hair.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        tail = hair = ListNode(None, head)
        for index in range(length//k):
            tail.next, head, tail = *self.reverse(head, k), head
            if index==length//k -1:
                tail.next = head
        return hair.next
    def reverse(self, head, tail):


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        tail = hair = ListNode(None, head)
        for index in range(length//k):
            tail.next, head, tail = *self.reverse(head, k), head
            if index==length//k -1:
                tail.next = head
        return hair.next


        

        

        

        
# @lc code=end

