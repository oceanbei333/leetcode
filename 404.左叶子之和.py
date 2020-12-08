#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def func(root, is_left:bool):
            if not root:
                return 0
            if not root.left and not root.right and is_left:
                return root.val
            return func(root.left, True) + func(root.right, False)
        return func(root, False)
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, False)])
        res = 0
        while queue:
            root, is_left = queue.popleft()
            if not root.left and not root.right and is_left:
                res += root.val
            if root.left:
                queue.append((root.left, True))
            if root.right:
                queue.append((root.right, False))
        return res

        
# @lc code=end

