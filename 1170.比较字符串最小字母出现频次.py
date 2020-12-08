#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
from typing import Counter


from typing import List
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def func(s):
            return Counter(s)[min(s)]
        word_nusm = [func(s) for s in words ]
        result  = []
        for s in queries:
            s_count = func(s)
            result.append( sum(count > s_count for count in word_nusm ) )
        return result
        
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def func(s):
            return Counter(s)[min(s)]
        for index in range(len(words)):
            words[index] = func(words[index])
        words.sort(reverse=True)
        for index in range(len(queries)):
            s_count = func(queries[index])
            num = 0
            for count in words:
                if count > s_count:
                    num += 1
                else:
                    break
            queries[index] = num
        return queries
        
# @lc code=end

