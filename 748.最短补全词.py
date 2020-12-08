#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        c = Counter()
        for lettter in licensePlate.lower():
            if ord('a') <= ord(lettter) <= ord('z'):
                c[lettter] += 1
        res = None
        for word in words:
            w_c = Counter(word)
            for lettter, counter in c.items():
                if counter > w_c[lettter]:
                    break
            else:

                if not res:
                    res = word
                else:
                    if len(res) > len(word):
                        res = word
        return res
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        c = Counter()
        for lettter in licensePlate.lower():
            if ord('a') <= ord(lettter) <= ord('z'):
                c[lettter] += 1
        res = None
        for word in words:
            if not c-Counter(word):
                if not res:
                    res = word
                else:
                    if len(res) > len(word):
                        res = word
        return res
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char = [i.lower()  for i in licensePlate  if i.isalpha()]
        words=sorted(words, key=lambda x:len(x))

        for word in words:
            l= char.copy()
            for i in word:
                if i in l:
                    l.remove(i)
                    
                if not l:
                    return word

# @lc code=end

