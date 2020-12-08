#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.tilt = 0
        def get_total(root):
            if not root:
                return 0
            left = get_total(root.left)
            right = get_total(root.right)
            self.tilt += abs(right - left)
            return left + right + root.val
        get_total(root)
        return self.tilt

# @lc code=end

