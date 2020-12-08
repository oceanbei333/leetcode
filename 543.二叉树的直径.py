#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(root:TreeNode):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L+R)
            return max(L, R)+1
        depth(root)
        return self.ans

        
# @lc code=end

