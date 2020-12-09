#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        def bfs(root:TreeNode):
            queue = [root]
            while queue:
                res.append(max(root.val for root in queue))
                new_queue = []
                for root in queue:
                    if root.left:
                        new_queue.append(root.left)
                    if root.right:
                        new_queue.append(root.right)
                queue = new_queue
        bfs(root)
        return res
    def largestValues(self, root: TreeNode) -> List[int]:
        vals = []
        def dfs(root, level):
            if not root:
                return
            if len(vals)>level:
                vals[level].append(root.val)
            else:
                vals.append([root.val])
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return [max(nums) for nums in vals]

# @lc code=end

