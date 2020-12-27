#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s)-1
        while l <= r and s[l] == ' ':
            l += 1
        while l <= r and s[r] == ' ':
            r -= 1
        queue, word = [], []
        while l <= r:
            if s[l] == ' ' and word:
                queue.append(''.join(word))
                word = []
            elif s[l] != ' ':
                word.append(s[l])
            l += 1
        queue.append(''.join(word))
        return ' '.join(queue[::-1])

# @lc code=end
