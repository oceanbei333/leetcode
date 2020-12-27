#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        target = sorted(p)
        len_p = len(p)
        for i in range(0, len(s)-len_p+1):
            if sorted(s[i:i+len_p]) == target:
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        from collections import Counter
        target, counter = Counter(p), Counter()
        len_p = len(p)
        for i in range(len(s)):
            counter[s[i]] += 1
            if i >= len_p:
                counter[s[i-len_p]] -= 1
            if counter & target == target:
                res.append(i-len_p+1)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter, p_counter, res = [0]*26, [0]*26, []
        for c in p:
            p_counter[ord(c)-ord('a')] += 1
        len_p = len(p)
        for i in range(len(s)):
            counter[ord(s[i])-ord('a')] += 1
            if i >= len_p:
                counter[ord(s[i-len_p])-ord('a')] -= 1
            if counter == p_counter:
                res.append(i-len_p+1)
        return res

# @lc code=end
