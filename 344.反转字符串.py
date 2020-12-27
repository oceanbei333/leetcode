#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index], s[-index-1] = s[-index-1], s[index]

    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

    def reverseString(self, s: List[str]) -> None:
        s.reverse()

    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            s.insert(i, s.pop())

# @lc code=end
