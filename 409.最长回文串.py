#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        has_even = False
        res = 0
        for count in counter.values():
            if count % 2:
                res += count-1
                has_even = True
            else:
                res += count
        return res + has_even
        
# @lc code=end

