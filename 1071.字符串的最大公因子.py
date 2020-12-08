#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ''
        for index in range(1, len(str2)+1):
            str3 = str1[:index]
            if not len(str1)%len(str3) and not len(str2)%len(str3):
                if not str1.replace(str3, '') and not str2.replace(str3, ''):
                    res = str3
        return res
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        length = gcd(len(str1), len(str2))
        str3 = str1[:length]
        if not str1.replace(str3, '') and not str2.replace(str3, ''):
            return str3
        return ''
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            return str1[:math.gcd(len(str1), len(str2))]
        return ""

# @lc code=end

