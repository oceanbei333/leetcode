#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        aset = set()
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            aset.add(root.val)
            dfs(root.right)
        dfs(root)
        return len(aset) == 1
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        aset = set()
        def dfs(root:TreeNode):
            if not root:
                return True
            aset.add(root.val)
            if len(aset) >1:
                return False
            return dfs(root.left) and dfs(root.right)
        return dfs(root)
    def isUnivalTree(self, root: TreeNode) -> bool:
        aset = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                aset.add(node.val)
                if len(aset) > 1:
                    return False
                stack.extend([node.left, node.right])
        return True

    def isUnivalTree(self, root: TreeNode) -> bool:
        left = not root.left or root.val == root.left.val and self.isUnivalTree(root.left)
        right = not root.right or root.val == root.right.val and self.isUnivalTree(root.right)
        return left and right
        

# @lc code=end

