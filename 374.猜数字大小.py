#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            num = guess(mid)
            if not num:
                return mid
            elif num == 1:
                low = mid +1
            else:
                high = mid -1
        return low
        
# @lc code=end

