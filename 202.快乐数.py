#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        aset = set()
        while n !=1 and n not in aset:
            aset.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            while num > 0:
                num, digit = divmod(num, 10)
                yield digit ** 2
        aset = set()
        while n !=1 and n not in aset:
            aset.add(n)
            n = sum(get_next(n))
        return n==1
        
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            while num > 0:
                num, digit = divmod(num, 10)
                yield digit ** 2
        slow = n
        fast = sum( get_next(n) )
        while fast != 1 and slow !=fast:
            slow=sum(get_next(slow))
            fast=sum(get_next( sum(get_next(fast)) ))
        return fast == 1
        
        

        
        
# @lc code=end

