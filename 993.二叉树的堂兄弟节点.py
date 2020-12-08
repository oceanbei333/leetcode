#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        queue = deque([( root, root )])
        while queue:
            adict = defaultdict(set)
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node:
                    adict[node.val].add(id(parent))
                    queue.append((node.left, node))
                    queue.append((  node.right, node ) )
            if adict[x]-adict[y] and adict[y]-adict[x]:
                return True
        return False
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        queue = deque([( root, root )])
        while queue:
            adict = dict()
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node:
                    adict[node.val] = id(parent)
                    queue.append((node.left, node))
                    queue.append((  node.right, node ) )
            if adict.get(x) and adict.get(y) and adict[x] != adict[y]:
                return True
        return False
# @lc code=end

