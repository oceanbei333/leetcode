#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        adict = dict()
        seq = 1
        for val in sorted(arr):
            if val not in adict:
                adict[val] = seq
                seq += 1
        for index in range(len(arr)):
            arr[index]=adict[arr[index]]
        return arr
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        adict = dict()
        for index, val in enumerate(sorted(set(arr))):
            if val not in adict:
                adict[val] = index+1
        for index in range(len(arr)):
            arr[index]=adict[arr[index]]
        return arr
         
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        adict = dict()
        for index, val in enumerate(sorted(set(arr))):
            if val not in adict:
                adict[val] = index+1
        return list( map(lambda index: adict[arr[index]], range(len(arr))) )
         
        
        
# @lc code=end

