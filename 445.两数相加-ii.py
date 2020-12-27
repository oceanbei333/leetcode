#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(l1):
            pre = None
            while l1:
                temp = l1.next
                l1.next = pre
                pre, l1 = l1, temp
            return pre
        l1, l2 = reverse(l1), reverse(l2)
        head = node = ListNode(None)
        plus = 0
        while l1 and l2:
            val = l1.val+l2.val+plus
            node.next = ListNode(val % 10)
            plus = val // 10
            node, l1, l2 = node.next, l1.next, l2.next
        l3 = l1 or l2
        while l3:
            val = l3.val + plus
            node.next = ListNode(val % 10)
            plus = val//10
            node, l3 = node.next, l3.next
        if plus:
            node.next = ListNode(plus)
        return reverse(head.next)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_number(node):
            res = 0
            while node:
                res *= 10
                res += node.val
                node = node.next
            return res

        def get_node(val: int):
            head = node = ListNode()
            for num in str(val):
                node.next = ListNode(int(num))
                node = node.next
            return head.next
        return get_node(get_number(l1)+get_number(l2))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2, pre, plus = [], [], None, 0
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 and stack2:
            val = stack1.pop()+stack2.pop() + plus
            plus = val//10
            node = ListNode(val % 10)
            node.next, pre = pre, node
        stack3 = stack1 or stack2
        while stack3:
            val = stack3.pop() + plus
            plus = val//10
            node = ListNode(val % 10)
            node.next, pre = pre, node
        if plus:
            node = ListNode(plus)
            node.next = pre
        return node


# @lc code=end
