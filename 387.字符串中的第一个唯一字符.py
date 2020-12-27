#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
    def firstUniqChar(self, s: str) -> int:
        aset = set()
        for i in range(len(s)):
            if s[i] not in aset:
                if len(s) - len(s.replace(s[i], '')) == 1:
                    return i
                aset.add(s[i])
        return -1
# @lc code=end
