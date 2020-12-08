#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        num = num1 + num2
        l3 = self.get_list_node(num)
        return l3

    def get_number(self, l1: ListNode) -> int:
        return int(''.join([str(i) for i in l1]))

    def get_list_node(self, number: int) -> ListNode:
        return [int(i) for i in str(number).split()]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        num = num1 + num2
        l3 = self.get_list_node(num)
        return l3

    def get_number(self, alist: ListNode) -> int:
        p = alist
        nums = []
        while p:
            nums.append(str(p.val))
            p = p.next
        return int(''.join(nums[::-1]))

    def get_list_node(self, number: int) -> ListNode:
        number_str = str(number)[::-1]
        alist = ListNode(number_str[0])
        p = alist
        for i in number_str[1:]:
            p.next = ListNode(i)
            p = p.next
        return alist


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        plus = 0
        node = None
        while node1 and node2:
            val1 = node1.val
            val2 = node2.val
            val = val1+val2 + plus
            val, plus = self.get_val(val, plus)
            node1 = node1.next
            node2 = node2.next
            if node:
                node.next = ListNode(val)
                node = node.next
            else:
                l3 = node = ListNode(val)
        left_node = node1 or node2
        while left_node:
            val = left_node.val + plus
            val, plus = self.get_val(val, plus)
            node.next = ListNode(val)
            node = node.next
            left_node = left_node.next
        if plus:
            node.next = ListNode(plus)
        return l3

    def get_val(self, val, plus):
        if val >= 10:
            plus = 1
            val = str(val)[1]
        else:
            plus = 0
        return val, plus


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        plus = 0
        node = self.get_node(l1, l2, plus)
        return node

    def get_node(self, node1: ListNode, node2: ListNode, plus: int) -> ListNode:
        if not node1 and not node2 and not plus:
            return
        val1 = node1.val if node1 else 0
        val2 = node2.val if node2 else 0
        val = val1 + val2 + plus
        current_val = val % 10
        plus = val // 10
        node = ListNode(current_val)
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
        node.next = self.get_node(node1, node2, plus)
        return node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode()
        plus = 0
        while l1 or l2 or plus:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + plus
            current_val = val % 10
            plus = val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p.next = ListNode(current_val)
            p = p.next
        return head.next


# @lc code=end
