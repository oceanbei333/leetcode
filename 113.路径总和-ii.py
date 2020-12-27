#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []

        def dfs(root: TreeNode, sum: int, path: List[int]):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if root.val == sum:
                    self.res.append(path)
                    return
            dfs(root.left, sum-root.val, path.copy())
            dfs(root.right, sum-root.val, path.copy())
        dfs(root, sum, [])
        return self.res

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, root.val, [root.val])]
        res = []
        while queue:
            new_queue = []
            for node, total, path in queue:
                if not node.left and not node.right and total == sum:
                    res.append(path)
                if node.left:
                    new_queue.append(
                        (node.left, total+node.left.val, path+[node.left.val]))
                if node.right:
                    new_queue.append(
                        (node.right, total+node.right.val, path+[node.right.val]))
            queue = new_queue
        return res
# @lc code=end
