#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = t
        def is_same(s: TreeNode, t: TreeNode)-> bool:
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return is_same(s.left, t.left) and is_same(s.right, t.right)
            return False

        def dfs(s:TreeNode)->bool:
            if not s:
                return False
            return is_same(s, self.t) or dfs(s.left) or dfs(s.right)
        return dfs(s)
        
# @lc code=end

