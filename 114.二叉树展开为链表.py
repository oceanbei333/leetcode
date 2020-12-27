#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.right = left
        node, next_ = root, root.right
        while next_:
            node.left, node, next_ = None, next_, next_.right
        node.right = right
        return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = list()

        def dfs(root):
            if not root:
                return
            nodes.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if not nodes:
            return
        pre = nodes[0]
        for node in nodes[1:]:
            pre.left = None
            pre.right = node
            pre = node

# @lc code=end
