#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        target = ( sum(A) -sum(B) )/2
        aset = {val -target for  val in A}
        for val in B:
            if val in aset:
                return [val+target, val]
        
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        target = ( sum(A) -sum(B) )/2
        aset = set(A)
        for val in B:
            if val+target in aset:
                return [val+target, val]
        
# @lc code=end

