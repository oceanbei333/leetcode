#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from typing import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for s in "!?',;.":
            paragraph=paragraph.replace(s, ' ')
        paragraph=paragraph.replace("  ", ' ')
        words= paragraph.lower().split(' ')
        counter = Counter(words)
        max = 0
        res = ''
        banned = set(banned)
        for word, count in counter.items():
            if word not in banned and count > max:
                res = word
                max = count
        return res
        
# @lc code=end

