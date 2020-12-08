#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        f = [[0]*26 for _ in range(t_len)]
        f.append([-1]*26)
        for index in range(t_len):
            ord_c = ord(t[-index-1])
            for i in range(26):
                if ord_c - ord('a') == i:
                    f[-index-2][i] = t_len -index -1
                else:
                    f[-index-2][i] = f[-index-1][i]
        cur = 0
        for index in range(s_len):
            s_c_index = f[cur][ord(s[index])-ord('a')]
            if  s_c_index == -1:
                return False
            else:
                cur = s_c_index + 1
        return True
    def isSubsequence(self, s: str, t: str) -> bool:
        i, m = 0, 0
        j, n = len(s), len(t)
        while i<j and m<n:
            if s[i] == t[m]:
                i+=1
            m += 1
        return i == j
        




# @lc code=end

