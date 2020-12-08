#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        alist = []
        def dfs(root:TreeNode,):
            if not root:
                return
            dfs(root.left)
            alist.append(root.val)
            dfs(root.right)
        dfs(root)
        min_val = float('inf')
        for index in range(len(alist)-1):
            min_val = min(min_val, alist[index+1]-alist[index])
        return min_val
            
# @lc code=end

