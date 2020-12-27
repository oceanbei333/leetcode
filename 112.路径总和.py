#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        new_sum = sum - root.val
        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            new_queue = []
            for node, val in queue:
                if not node.left and not node.right and val == sum:
                    return True
                if node.left:
                    new_queue.append((node.left, val+node.left.val))
                if node.right:
                    new_queue.append((node.right, val+node.right.val))
            queue = new_queue
        return False


# @lc code=end
