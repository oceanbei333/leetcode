#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        length = len(S)
        pre = - length
        res = []
        for index in range(length):
            if S[index] == C:
                res.append(0)
                pre = index
            else:
                res.append(index-pre)
        pre = -length
        for index in range(1, length+1):
            if S[-index] == C:
                pre = index
            else:
                res[-index] = min(res[-index], index-pre)
        return res
# @lc code=end

