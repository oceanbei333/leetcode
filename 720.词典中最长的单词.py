#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        aset = set(words)
        res = ''
        for word in words:
            if len(word) > len(res) or len(word) == len(res) and word < res:
                if all(word[:k] in aset for k in range(1, len(words))):
                    res = word
        return res
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        for i, word in enumerate(words):
            functools.reduce(lambda x,y: x[y], word, trie)['index'] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if 'index' in cur:
                word = words[cur['index']]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                for letter in cur:
                    if letter != 'index':
                        stack.append(cur[letter])

        return ans

# @lc code=end

