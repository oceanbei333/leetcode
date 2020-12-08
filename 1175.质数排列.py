#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return [1]
        def is_prime(n:int):
            if not n%2:
                return False
            for num in range(3,int(n**0.5+1), 2):
                if not n%num:
                    return False
            return True
        res = list(range(1, n+1))
        res[1] = 2
        index = 2
        for num in range(3, n+1):
            if is_prime(num):
                res[num-1], res[index] = res[index], res[num-1]
        return res
# @lc code=end

