#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        count_i = 0
        count_d = 0
        res = []
        N = len(S)+1
        for s in S:
            if s == "I":
                res.append(count_i)
                count_i += 1
            else:
                res.append(N-1-count_d)
                count_d += 1
        if S[-1] == "I":
            res.append(count_i)
        else:
            res.append(N-1-count_d)
        return res
    def diStringMatch(self, S: str) -> List[int]:
        count_i = 0
        count_d = 0
        res = []
        S += S[-1]
        N = len(S)
        for s in S:
            if s == "I":
                res.append(count_i)
                count_i += 1
            else:
                res.append(N-1-count_d)
                count_d += 1
        return res
    def diStringMatch(self, S: str) -> List[int]:
        i, j = 0, len(S)
        res = []
        for s in S:
            if s == "I":
                res.append(i)
                i+= 1
            else:
                res.append(j)
                j -= 1
        return res + [j]

# @lc code=end

