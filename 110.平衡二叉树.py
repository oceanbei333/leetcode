#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def isBalanced(self, root: TreeNode) -> bool:
        @lru_cache(None)
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return (abs(height(root.left) - height(root.right)) <= 1 
        and self.isBalanced(root.left) 
        and self.isBalanced(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        def height(root:TreeNode) ->int:
            if not root:
                return 0
            left_heght = height(root.left)
            right_heght = height(root.right)
            if left_heght == -1 or right_heght == -1 or abs(left_heght-right_heght) >1:
                return -1
            else:
                return max(left_heght, right_heght)+1
        return height(root)  != -1

            

# @lc code=end

