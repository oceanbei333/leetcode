#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
    def removeDuplicates(self, S: str) -> str:
        pre_len = -1
        while pre_len != len(S):
            pre_len = len(S)
            aset = set(S)
            for s in aset:
                S = S.replace(s*2, "")
        return S


        
# @lc code=end

