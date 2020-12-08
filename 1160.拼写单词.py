#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
from typing import Counter, List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        return sum(len(s) for s in words if all(count <= counter.get(c, 0)  for c, count in Counter(s).items()))
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        result = 0
        for s in words:
            if all(count <= counter.get(c, 0) for c, count in Counter(s).items()):
                result += len(s)
        return result
            


        
# @lc code=end

