#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        alist = []
        while head:
            alist.append(head.val)
            head = head.next
        return all(alist[index]==alist[-index-1] for index in range(len(alist)//2))
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        node = head
        length = 0
        while node:
            length+=1
            node = node.next
        node = head
        pre = None
        for _ in range(length//2):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        if length % 2:
            node2 = node.next
        else:
            node2 = node
        node1 = pre
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
    def isPalindrome(self, head: ListNode) -> bool:
        self.front = head
        def check(cur:ListNode)->bool:
            if cur:
                if not check(cur.next):
                    return False
                if cur.val != self.front.val:
                    return False
                self.front = self.front.next
            return True
        return check(head)


        
        
# @lc code=end

