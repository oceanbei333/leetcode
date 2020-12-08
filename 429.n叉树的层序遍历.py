#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            alist = []
            for _ in range(len(queue)):
                root = queue.popleft()
                alist.append(root.val)
                queue.extend(root.children)
            res.append(alist)
        return res
        
# @lc code=end

