#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        first = root
        while first:
            last, next_first,head = None, None, first
            while head:
                if head.left:
                    if last:
                        last.next = head.left
                    last = head.left
                    next_first = next_first or last
                if head.right:
                    if last:
                        last.next = head.right
                    last = head.right
                    next_first = next_first or last
                head = head.next
            first = next_first
        return root


# @lc code=end
