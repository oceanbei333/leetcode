#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        for index in range(len(haystack)+1-length):
            if haystack[index:index+length] == needle:
                return index
        return -1
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        for index in range(len(haystack)+1-length):
            for i in range(length):
                if haystack[index+i] != needle[i]:
                    break
            else:
                return index
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        needle_hasd = hash(needle)
        for index in range(len(haystack)+1-length):
            if hash(haystack[index:index+length])==needle_hasd :
                return index
        return -1
# @lc code=end

