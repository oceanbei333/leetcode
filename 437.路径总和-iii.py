#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            cur = [val+root.val for val in left+right] + [root.val]
            self.res += cur.count(sum)
            return cur
        dfs(root)
        return self.res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0

        def dfs(root, path):
            if not root:
                return
            total = path[-1] + root.val
            for num in path:
                if total - num == sum:
                    self.count += 1
            dfs(root.left, path+[total])
            dfs(root.right, path+[total])
        dfs(root, [0])
        return self.count


# @lc code=end
