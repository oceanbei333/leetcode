#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_n = abs(arr[0]-arr[1])
        for index in range(1, len(arr)-1):
            min_n = min(min_n, abs(arr[index]-arr[index+1]))
        result = []
        for index in range(len(arr)-1):
            if abs(arr[index]-arr[index+1]) == min_n:
                result.append((arr[index], arr[index+1]))
        return result

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_n = abs(arr[0]-arr[1])
        for index in range(1, len(arr)-1):
            min_n = min(min_n, abs(arr[index]-arr[index+1]))
        return list([arr[index], arr[index+1]] for index in range(len(arr)-1) if abs(arr[index]-arr[index+1]) == min_n)


    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = [[arr[0], arr[1]]]
        min_n = abs(arr[0]-arr[1])
        for index in range(1, len(arr)-1):
            abs_n = abs(arr[index] - arr[index+1])
            if abs_n < min_n:
                result = [[arr[index], arr[index+1]]]
                min_n = abs_n
            elif abs_n == min_n:
                result.append([arr[index], arr[index+1]])
        return result


        
# @lc code=end

