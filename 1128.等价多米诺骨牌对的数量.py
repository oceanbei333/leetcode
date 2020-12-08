#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairNum = 0
        for i in range(len(dominoes)-1):
            for j in range(i+1, len(dominoes)):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1] :
                    pairNum += 1
                elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    pairNum += 1
        return pairNum
                
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        adict = defaultdict(int)
        for val1, val2 in dominoes:
            if val1 < val2:
                val1, val2 = val2, val1
            adict[(val1, val2)] += 1
        return sum(map( lambda x: x*(x-1)//2 ,adict.values() ))
            
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        adict = defaultdict(int)
        for val1, val2 in dominoes:
            if val1 < val2:
                val1, val2 = val2, val1
            adict[(val1, val2)] += 1
        total = 0
        for val  in adict.values():
            total += val*(val-1)//2
        return total
        
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        total = 0
        adict = dict()
        for val1, val2 in dominoes:
            if val1 < val2:
                val1, val2 = val2, val1
            adict[(val1, val2)] = adict.get((val1, val2),0) + 1
            total += adict[(val1, val2)] -1
        return total
# @lc code=end

