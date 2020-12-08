#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <3:
            return False
        aset = set()
        for index in range(len(A)):
            if not index:
                continue
            if A[index-1] < A[index]:
                if 0 in aset:
                    return False
                aset.add(1)
            elif A[index-1] > A[index]:
                if  1 not in aset:
                    return False
                aset.add(0)
            else:
                return False
        if len(aset) == 2:
            return True

    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        length = len(A)
        while i < length-1  and A[i]<A[i+1]:
            i += 1
        if not i or i == length-1:
            return False
        while i < length-1 and A[i]>A[i+1]:
            i += 1
        return i == length-1


        
# @lc code=end

