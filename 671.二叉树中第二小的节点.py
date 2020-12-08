#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_v  = root.val
        self.sec_v = None
        def dfs(root: TreeNode):
            if not root:
                return
            if self.sec_v is not None and root.val > self.sec_v:
                return 
            elif root.val == min_v:
                dfs(root.left)
                dfs(root.right)
            else:
                self.sec_v = root.val
        dfs(root)
        return -1 if self.sec_v is None else self.sec_v



            
# @lc code=end

