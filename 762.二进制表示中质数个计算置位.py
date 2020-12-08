#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def is_prime(n:int)->bool:
            if n == 1:
                return False
            if n == 2:
                return True
            if not n%2:
                return False
            for num in range(3,int( n**0.5+1 ), 2):
                if not n%num:
                    return False
            return True

        return sum(is_prime(bin(n)[2:].count('1')) for n in range(L, R+1) )
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(n)[2:].count('1') in primes for n in range(L, R+1) )

        
# @lc code=end

