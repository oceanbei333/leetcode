#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s%3:
            return False
        num =s//3
        i = 0
        while i < len(A)-1:
            if A[i] == num:
                i += 1
                break
            A[i+1] += A[i]
            i += 1
        while i < len(A)-1:
            if A[i] == num:
                print(i)
                return True
            A[i+1] += A[i]
            i += 1
        return False
            

# @lc code=end

