#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode,alist:list):
            if not root:
                return
            if not root.left and not root.right:
                alist.append(root.val)
            dfs(root.left, alist)
            dfs(root.right, alist)
        list1 = []
        dfs(root1, list1)
        list2 = []
        dfs(root2, list2)
        return list1 == list2

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode)->str:
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val) + ','
            else:
                return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)

        
# @lc code=end

