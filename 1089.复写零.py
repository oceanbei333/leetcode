#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        alist = []
        for num in arr:
            if not num:
                alist.extend([0,0])
            else:
                alist.append(num)
        for index in range(len(arr)):
            arr[index] = alist[index]
    def duplicateZeros(self, arr: List[int]) -> None:
        alist = arr[::-1].copy()
        index = 0
        length = len(arr)
        while index < length:
            val = alist.pop()
            arr[index] = val
            index += 1
            if not val and index<length:
                arr[index] = 0
                index += 1

    def duplicateZeros(self, arr: List[int]) -> None:
        zero_n = arr.count(0)
        length = len(arr)
        for index in range(length-1, -1, -1):
            if index + zero_n < length:
                arr[index+zero_n] = arr[index]
            if not arr[index]:
                zero_n -= 1
                if index + zero_n < length:
                    arr[index+zero_n] = 0


# @lc code=end

