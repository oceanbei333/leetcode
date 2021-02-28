#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Union


class Solution:
    def minDepth(self, root: TreeNode) -> Union[int, float]:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif root.left:
            return self.minDepth(root.left)+1
        return self.minDepth(root.right)+1

    def minDepth(self, root: TreeNode) -> Union[int, float]:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return float('inf')
            if not root.left and not root.right:
                return 1
            return min(dfs(root.left), dfs(root.right))+1
        return dfs(root)

    def minDepth(self, root: TreeNode) -> Union[int, float]:
        if not root:
            return 0
        depth, queue = 0, [root]
        while queue:
            new_queue = []
            depth += 1
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue


# @lc code=end
