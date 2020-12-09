#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(root:TreeNode)->str:
            if not root:
                return ''
            if not root.left and not root.right:
                return str(root.val)
            elif root.left and root.right:
                return f"{root.val}({dfs(root.left)})({dfs(root.right)})"
            elif root.left:
                return f"{root.val}({dfs(root.left)})"
            else:
                return f"{root.val}()({dfs(root.right)})"
        return dfs(t)
        
# @lc code=end

