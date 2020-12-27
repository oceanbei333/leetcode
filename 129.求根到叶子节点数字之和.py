#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, root.val)]
        res = 0
        while queue:
            new_queue = []
            for node, total in queue:
                if not node.left and not node.right:
                    res += total
                else:
                    if node.left:
                        new_queue.append((node.left, total*10+node.left.val))
                    if node.right:
                        new_queue.append((node.right, total*10+node.right.val))
                queue = new_queue
        return res

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, total):
            if not root.left and not root.right:
                return total
            res = 0
            if root.left:
                res += dfs(root.left, total*10+root.left.val)
            if root.right:
                res += dfs(root.right, total*10+root.right.val)
            return res
        return dfs(root, root.val)

# @lc code=end
