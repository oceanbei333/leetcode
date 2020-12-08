#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(root: TreeNode):
            if not root:
                return 
            if root.val < low:
                return dfs(root.right)
            elif root.val > high:
                return dfs(root.left)
            else:
                root.left = dfs(root.left)
                root.right = dfs(root.right)
                return root
        return dfs(root)
            
        
# @lc code=end

