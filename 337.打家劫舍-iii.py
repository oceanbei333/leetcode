#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dp(root, flag: bool):
            if not root:
                return 0
            profit = dp(root.left, False) + dp(root.right, False)
            if not flag:
                profit = max(profit, root.val + dp(
                    root.left, True) + dp(root.right, True))
            return profit
        return dp(root, False)

    def rob(self, root: TreeNode) -> int:
    # 尾递归优化
        def dp(root):
            if not root:
                return 0, 0
            left = dp(root.left)
            right = dp(root.right)
            profit_yes = root.val + left[0] + right[0]
            profit_no = max(left) + max(right)
            return profit_no, profit_yes
        return max(dp(root))


# @lc code=end
