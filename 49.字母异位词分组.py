#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict
        adict = defaultdict(list)
        for word in strs:
            counter = Counter(word)
            adict[counter].append(word)
        return list(adict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        adict = defaultdict(list)
        for word in strs:
            adict[tuple(sorted(word))].append(word)
        return list(adict.values())
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        adict = defaultdict(list)
        for word in strs:
            key = [0]*26
            for s in word:
                key[ord(s)-ord('a')]+=1
            adict[tuple(key)].append(word)
        return list(adict.values())
# @lc code=end

