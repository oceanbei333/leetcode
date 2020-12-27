#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return
        pre = []
        queue = [root]
        while queue:
            pre = queue
            queue = [child for node in queue for child in (
                node.left, node.right) if child]
        return pre[0].val

# @lc code=end
