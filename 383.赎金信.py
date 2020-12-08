#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter = Counter(magazine)
        counter.subtract(Counter(ransomNote))
        return all(c>=0 for c in counter.values())
# @lc code=end

