#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from typing import List


class Solution:
    def findLadders(self, beginWord, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        c_set = {chr(ord('a')+i) for i in range(26)}
        queue = [(beginWord, [beginWord])]
        cost = {word: float('inf') for word in wordList}
        cost[beginWord] = 0
        length = len(beginWord)
        res = list()
        while queue and not res:
            new_queue = []
            for word, path in queue:
                if word == endWord:
                    res.append(path)
                    continue
                for i in range(length):
                    for s in c_set-{word[i]}:
                        new_word = word[:i]+s+word[i+1:]
                        if new_word in word_set and cost[new_word] >= cost[word]+1:
                            cost[new_word] = cost[word]+1
                            new_queue.append((new_word, path+[new_word]))
            queue = new_queue
        return res


# @lc code=end
