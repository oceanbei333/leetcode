#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def _postorder(root: 'Node'):
            if not root:
                return
            for node in root.children:
                _postorder(node)
            res.append(root.val)
        _postorder(root)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.extend(root.children)
        return res[::-1]
