#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
        for length in range(1, n+1):
            for start in range(n-length+1):
                end = start + length - 1
                for i in range(start, end+1):
                    for l in dp[start][i-1] or [None]:
                        for r in dp[i+1][end] or [None]:
                            root = TreeNode(i+1, l, r)
                            dp[start][end].append(root)
        return dp[0][n-1]

    def generateTrees(self, n: int) -> List[TreeNode]:
        @lru_cache(n**2)
        def dp(start: int, end: int):
            return [TreeNode(i, l, r) for i in range(start, end+1) for l in dp(start, i-1) or [None] for r in dp(i+1, end) or [None]]
        return dp(1, n)


# @lc code=end
