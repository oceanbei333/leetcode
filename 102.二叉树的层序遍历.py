#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            res.append([node.val  for node in stack] )
            a_stack = []
            for node in stack:
                if node.left:
                    a_stack.append(node.left)
                if node.right:
                    a_stack.append(node.right)
            stack = a_stack
        return res
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque([ root ])
        res = []
        while queue:
            res.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res



# @lc code=end

