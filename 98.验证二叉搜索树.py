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
        def helper(root: TreeNode, low, high) -> bool:
            if not root:
                return True
            val = root.val
            if val <= low or val >= high:
                return False
            return helper(root.left, low, val) and helper(root.right, val, high)
        return helper(root, float('-inf'), float('inf'))

    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = float('-inf')
        def dfs(root) -> bool:
            if not root:
                return True
            if not dfs(root.left):
                return False
            if root.val <= self.pre:
                return False
            self.pre = root.val
            if not dfs(root.right):
                return False
            return True
        return dfs(root)

    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True



# @lc code=end
