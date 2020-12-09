#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



# @lc code=end

