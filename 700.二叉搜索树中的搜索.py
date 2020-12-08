#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root:TreeNode)-> TreeNode:
            if not root:
                return 
            if root.val == val:
                return root
            elif root.val < val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        return dfs(root)
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right

        
# @lc code=end

