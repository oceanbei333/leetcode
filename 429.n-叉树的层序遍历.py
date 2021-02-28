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
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            new_queue, alist = [], []
            for node in queue:
                alist.append(node.val)
                new_queue.extend(node.children)
            res.append(alist)
            queue = new_queue
        return res

# @lc code=end
