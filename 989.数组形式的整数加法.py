#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list( map(int,  str( int( ''.join( map(str, A) ) ) + K ) ) )
        
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        alist = list(map(int, str(K)))
        if len(alist) > len(A):
            A , alist = alist, A
        result = []
        plus = 0
        for index in range(len(alist)):
            val = alist[-index-1] + A[-index-1] + plus
            result.append(val % 10)
            plus = val // 10
        for index in range(0, len(A)-len(alist)):
            val = A[-index-1-len(alist)] + plus
            result.append(val % 10)
            plus = val // 10
        if plus:
            result.append(plus)
        return result[::-1]

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        plus = K
        for index in range( len(A) ):
            val = A[-index-1] + plus
            A[-index-1] = val % 10
            plus = val // 10
        if plus:
            A = list( map(int, str(plus)) ) + A
        return A


                



# @lc code=end

