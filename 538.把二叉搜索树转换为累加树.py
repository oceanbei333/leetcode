#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root or not root.left and not root.right:
            return root
        self.pre = 0

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.pre += root.val
            root.val = self.pre
            dfs(root.left)
        dfs(root)
        return root


# @lc code=end
