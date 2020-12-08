#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Optional, Union


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return sorted(res) == res and len(res) == len(set(res))

    def isValidBST(self, root: TreeNode) -> bool:
        def func(root: TreeNode, low:Union[int, float], high:Union[int, float])->bool:
            if not root:
                return True
            val = root.val
            if val <= low or val >= high:
                return False
            return func(root.left, low, val) and func(root.right, val, high)
        return func(root, float('-inf'), float('inf'))
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def dfs(root: TreeNode)->bool:
            if not root:
                return True
            if not dfs(root.left):
                return False
            if res and root.val <= res[-1]:
                return False
            res.append(root.val)
            if not dfs(root.right):
                return False
            return True
        return dfs(root)

    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None and root.val <=pre:
                return False
            pre = root.val
            root = root.right
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        pre = None
        def dfs(root: TreeNode)->bool:
            if not root:
                return True
            if not dfs(root.left):
                return False
            nonlocal pre
            if pre is not None and root.val <= pre:
                return False
            pre = root.val
            if not dfs(root.right):
                return False
            return True
        return dfs(root)
# @lc code=end

