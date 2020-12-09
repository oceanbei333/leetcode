#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def _preorder(root: 'Node'):
            if not root:
                return
            res.append(root.val)
            for node in root.children:
                _preorder(node)
        _preorder(root)
        return res

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        while root:
            res.append(root.val)
            stack.extend(root.children[::-1])
            root = stack.pop() if stack else None
        return res
            
        
# @lc code=end

