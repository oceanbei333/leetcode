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
        for index, c in enumerate(s):
            if counter[c] == 1:
                return index
        return -1
# @lc code=end

