#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for index in range(len(digits)-1, -1, -1):
            val = digits[index] + plus
            digits[index] = val % 10
            plus = val // 10
        if plus:
            digits.insert(0, 1)
        return digits
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        plus = 1
        from collections import deque
        queue = deque()
        while digits:
            val = digits.pop() + plus
            queue.appendleft(val%10)
            plus = val //10
        if plus:
            queue.appendleft(plus)
        return list(queue)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] !=9:
                digits[i]+= 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
        
# @lc code=end
