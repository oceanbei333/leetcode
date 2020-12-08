#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root: 'Node') -> int:
            if not root:
                return 0
            if not root.children:
                return 1
            return max(dfs(node) for node in root.children) + 1
        return dfs(root)

        
# @lc code=end

