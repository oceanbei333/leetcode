#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            res = max(res, len(stack))
            if c=='(':
                stack.append(1)
            elif c == ')':
                stack.pop()
        return res
# @lc code=end

