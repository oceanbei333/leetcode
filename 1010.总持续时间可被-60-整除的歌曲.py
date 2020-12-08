#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        adict = dict()
        for index in range(len(time)):
            targt_time =  time[index] % 60
            if targt_time in adict:
                adict[targt_time] += 1
            else:
                adict[time[index] %60 ] = 1
        total = 0
        for i in set( range(0,31) ) & set(adict.keys()):
            if i in {0, 30}:
                num = adict.get(i)
                if num and num > 1:
                    total += num*(num-1)//2
            else:
                num1 = adict.get(i)
                num2 = adict.get(60-i)
                if num2 and num1:
                    total += num1*num2
        return total

            
        
# @lc code=end

