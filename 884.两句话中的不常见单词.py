#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from typing import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a_counter = Counter(A.split(" "))
        b_counter = Counter(B.split(" "))
        res = []
        for word, counter in a_counter.items():
            if counter == 1 and not b_counter[word]:
                res.append(word)
        for word, counter in b_counter.items():
            if counter == 1 and not a_counter[word]:
                res.append(word)
        return res
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
       return [ word for word, count in Counter(A.split(" ")+B.split(" ")).items() if count ==1 ]

       
# @lc code=end

