#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "")
        length = len(S)
        if length % K:
            start = length % K
            res = S[:start].upper()
        else:
            start = 0
            res = ''
        for index in range(start, length, K):
            if not index:
                res = S[index: index+K].upper()
            else:
                res = f"{res}-{ S[index: index+K].upper() }"
        return res
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        count = 0
        res =  ''
        for index in range(len(S)):
            if S[-index-1] !='-':
                if not count%K and res:
                    res += '-'
                res += S[-index-1].upper()
                count += 1
        return res[::-1]

        
# @lc code=end

