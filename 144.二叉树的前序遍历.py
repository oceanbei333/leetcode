#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return res
# @lc code=end
