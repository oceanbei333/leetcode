#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)

            arrow_left = arrow_right = 0
            if root.left and root.left.val == root.val:
                arrow_left = left_len+1
            if root.right and root.right.val == root.val:
                arrow_right = right_len+1
            self.res = max(self.res, arrow_left+arrow_right)
            return max(arrow_left, arrow_right)
        dfs(root)
        return self.res
# @lc code=end
