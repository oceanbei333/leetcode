#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(" ")[::-1])[::-1]
        
# @lc code=end

