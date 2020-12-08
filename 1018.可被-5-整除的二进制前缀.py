#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = [not A[0] % 5]
        for index in range(1, len(A)):
            A[index] += A[index-1]<< 1
            result.append(not A[index] % 5)
        return result

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        pre = A[0]
        A[0] = not A[0] % 5
        for index in range(1, len(A)):
            val =  (pre << 1) + A[index]
            A[index] = not val % 5
            pre = val
        return A


        
# @lc code=end

