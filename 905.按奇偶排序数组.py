#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        index = 0
        length = len(A)
        while index < length:
            if A[index] % 2:
                A[index], A[length-1] = A[length-1], A[index]
                length -= 1
            else:
                index += 1
        return A

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x %2)
        return A
        
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if not x%2] + [x for x in A if x%2]



# @lc code=end

