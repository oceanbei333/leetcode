#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def func(root: TreeNode, alist: list):
            if not root:
                return
            alist = deepcopy(alist)
            alist.append(str( root.val ))
            if not root.left and not root.right:
                res.append('->'.join(alist))
            else:
                func(root.left, alist)
                func(root.right, alist)
        func(root, [])
        return res
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def func(root: TreeNode, s:str):
            if not root:
                return
            s += str(root.val) 
            if not root.left and not root.right:
                res.append(s)
            else:
                s += '->'
                func(root.left, s)
                func(root.right, s)
        func(root, '')
        return res
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        from collections import deque
        queue = deque([ [root, str(root.val)] ])
        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()
                if not node.left and not node.right:
                    res.append(path)
                if node.left:
                    queue.append([node.left, f"{path}->{str(node.left.val)}" ])
                if node.right:
                    queue.append([node.right, f"{path}->{str(node.right.val)}" ])
        return res





            
# @lc code=end

