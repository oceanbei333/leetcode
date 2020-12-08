#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.set = set()
        def dfs(root:TreeNode)->bool:
            if not root:
                return False
            if root.val in self.set:
                return True
            else:
                self.set.add(k-root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
        
# @lc code=end

