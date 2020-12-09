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
    def reverse(self, head:ListNode, length:int)->ListNode:
        pre = None
        node = head
        for _ in range(length):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        tail = head
        new_head = pre
        next_head = node
        return new_head, tail ,next_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length+= 1
            node = node.next
        hair = ListNode()
        tail = hair
        node = head
        for _ in range(length//k):
            new_head, new_tail, next_head = self.reverse(node, k)
            tail.next = new_head
            tail = new_tail
            node = next_head
        if length %k:
            tail.next = next_head
        return hair.next


    def reverse(self, head:ListNode, tail:ListNode)->ListNode:
        """
        swap tow node, 
        and point last to next node for the case of less k node
        """
        pre = tail.next
        while pre is not tail:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = hair = ListNode(None, head)
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            pre.next = tail
            pre = head
            head = self.reverse(head, tail)
        return hair.next
        
    def reverse(self, head:ListNode, length:int)->ListNode:
        """
        swap tow node, 
        and point last to next node for the case of less k node
        """
        pre = None
        node = head
        for _ in range(length):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        head.next = node
        return pre, node

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length+= 1
            node = node.next
        tail = hair = ListNode(None, head)
        for _ in range(length//k):
            tail.next, head, tail = *self.reverse(head, k), head
        return hair.next
# @lc code=end

