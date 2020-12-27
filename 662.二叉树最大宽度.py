#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue, indexes = deque([root]), deque([1])
        res = 0
        while queue:
            res = max(res, indexes[-1]-indexes[0]+1)
            for _ in range(len(queue)):
                node, index = queue.popleft(), indexes.popleft()
                if node.left:
                    indexes.append(index*2)
                    queue.append(node.left)
                if node.right:
                    indexes.append(index*2+1)
                    queue.append(node.right)
        return res


# @lc code=end
