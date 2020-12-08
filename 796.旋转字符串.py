#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        for index in range(1,len(A)):
            if A[index:]+A[:index] == B:
                return True
        return False
        
    def rotateString(self, A: str, B: str) -> bool:
        return len(B)==len(A) and B in A+A
# @lc code=end

