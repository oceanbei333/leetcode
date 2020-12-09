#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from typing import DefaultDict, List, NewType, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict

        def get_edge(wordList: List[str]) -> DefaultDict[str, List[str]]:
            edge = defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    new_word = word[:i]+'*'+word[i+1:]
                    edge[new_word].append(word)
                    edge[word].append(new_word)
            return edge
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        edge = get_edge(wordList)

        dis_begin, dis_end = defaultdict(int), defaultdict(int)
        queue_begin, queue_end = [beginWord], [endWord]

        while queue_begin and queue_end:
            if len(queue_end) < len(queue_begin):
                queue_begin, queue_end = queue_end, queue_begin
                dis_begin, dis_end = dis_end, dis_begin
            new_queue_begin = []
            for word in queue_begin:
                if dis_end[word]:
                    return (dis_begin[word]+dis_end[word])//2 + 1
                for next_word in edge[word]:
                    if not dis_begin[next_word]:
                        dis_begin[next_word] = dis_begin[word]+1
                        new_queue_begin.append(next_word)
            queue_begin = new_queue_begin
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        unvisited = set(wordList)
        if endWord not in unvisited:
            return 0
        length = len(beginWord)
        begin, end = {beginWord}, {endWord}
        count = 1
        c_set = {chr(ord('a')+i) for i in range(26)}
        while begin and end:
            count += 1
            new_begin = set()
            for word in begin:
                for i in range(length):
                    for s in c_set-{word[i]}:
                        new_word = word[:i]+s+word[i+1:]
                        if new_word in end:
                            return count
                        if new_word in unvisited:
                            unvisited.remove(new_word)
                            new_begin.add(new_word)
            begin = new_begin
            if len(end) < len(begin):
                begin, end = end, begin
        return 0


# @lc code=end
