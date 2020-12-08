#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        length = len(words)
        first_sec = (first, second)
        res = []
        for index in range(length-1):
            if tuple(words[index: index+2]) == first_sec and index+2 < length:
                res.append(words[index+2])
        return res
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        length = len(words)
        res = []
        for index in range(length-1):
            if words[index]== first and words[index+1]==second and index+2 < length:
                res.append(words[index+2])
        return res
        
# @lc code=end

