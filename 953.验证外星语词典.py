#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_list = order
        def func(word):
            res = []
            for s in word:
                res.append(map_list.index(s))
            return res
        return sorted(words,key=func) == words
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_dict = {s: index for index, s in enumerate(order)}
        def func(word):
            return [ map_dict[s] for s in word ]
        return sorted(words,key=func) == words
# @lc code=end

