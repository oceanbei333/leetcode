#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        total = 0
        for val in Counter(s).values():
            total += val//2*2
            if not total%2 and val%2:
                total +=1
        return total 

# @lc code=end

