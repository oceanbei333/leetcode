#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        counter = defaultdict(int)
        self.res = []

        def dfs(root):
            if not root:
                return ''
            serial = f"{str(root.val)},{dfs(root.left)},{dfs(root.right)}"
            counter[serial] += 1
            if counter[serial] == 2:
                self.res.append(root)
            return serial
        dfs(root)
        return self.res

# @lc code=end
