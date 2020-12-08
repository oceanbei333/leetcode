#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alist = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        aset = set()
        for word in words:
            word_n = ''
            for s in word:
                word_n += alist[ord(s)-ord('a')]
            aset.add(word_n)
        return len(aset)

# @lc code=end

