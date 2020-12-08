#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def func(left:int, right):
            if left > right:
                return
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = func(left, mid-1)
            root.right = func(mid+1, right)
            return root
        return func(0, len(nums)-1)
# @lc code=end

