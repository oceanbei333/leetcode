#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Union


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def hight(root:TreeNode)-> int:
            if not root.left and not root.right:
                return 1
            if not root.left:
                return hight(root.right) + 1
            if not root.right:
                return hight(root.left) + 1
            return min(hight(root.left), hight(root.right)) +1
        return hight(root)

    def minDepth(self, root: TreeNode) -> Union[int, float]:
        if not root:
            return 0
        depth = 0
        from collections import deque
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                root = queue.popleft()
                if not root.left and not root.right:
                    return depth
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
    def minDepth(self, root: TreeNode) -> Union[int, float]:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif root.left:
            return self.minDepth(root.left)+1
        return self.minDepth(root.right)+1


# @lc code=end

