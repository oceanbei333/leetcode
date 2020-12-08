#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        adict = dict()
        for index in range(len(s)):
            if s[index] not in adict:
                if t[index] in adict.values():
                    return False
                adict[s[index]] = t[index]
            else:
                if adict[s[index]] != t[index]:
                    return False
        return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        adict = dict()
        aset = set()
        for index in range(len(s)):
            if s[index] not in adict:
                if t[index] in aset:
                    return False
                adict[s[index]] = t[index]
                aset.add(t[index])
            else:
                if adict[s[index]] != t[index]:
                    return False
        return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[index])==t.index(t[index]) for index in range(len(s)))

# @lc code=end

