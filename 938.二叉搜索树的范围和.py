#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Collection


from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def dfs(root):
            if not root:
                return 
            if L <= root.val <= R:
                self.total += root.val
            if root.val < R:
                dfs(root.right)
            if root.val > L:
                dfs(root.left)
        dfs(root)
        return self.total
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return
        queue = deque([ root ])
        total = 0
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if L <= node.val <= R:
                total += node.val
            if node.val < R:
                queue.append(node.right)
            if node.val > L:
                queue.append(node.left)
        return total
        
        
# @lc code=end

