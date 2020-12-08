#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_index = len(A) -1
        index = 0
        while index < len(A) and odd_index > 0:
            if A[index] % 2:
                A[index], A[odd_index] = A[odd_index], A[index]
                odd_index -= 2
            else:
                index += 2
        return A



        
# @lc code=end

