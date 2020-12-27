#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def dfs(root, key, parent):
            if not root:
                return None, None
            if root.val == key:
                return root, parent
            if root.val > key:
                return dfs(root.left, key, root)
            if root.val < key:
                return dfs(root.right, key, root)
        node, parent = dfs(root, key, None)
        if not node:
            return root

        def remove(node, parent):
            if node.left:
                parent.

# @lc code=end
