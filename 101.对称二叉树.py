#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(p:TreeNode, q:TreeNode) -> bool:
            if not p and not q:
                return True
            if not all((p, q)):
                return False
            return p.val == q.val and func(p.left, q.right) and func(p.right, q.left)
        return func(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root, root]
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            if not all((p, q)):
                return False
            if q.val != p.val:
                return False
            stack.extend([p.left,q.right, p.right, q.left])
        return True
        



        


# @lc code=end