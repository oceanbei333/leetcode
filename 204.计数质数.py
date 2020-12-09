#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
from typing import Counter


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        counter = 1
        for i in range(2, n):
            if not i%2:
                continue
            for j in range(3, int( i**0.5 )+1, 2):
                if not i%j:
                    break
            else:
                counter+=1
        return counter

    def countPrimes(self, n: int) -> int:
        if n< 3:
            return 0
        alist = [1]*n
        n_sqr = int(n**0.5)+1
        for i in range(2,n_sqr):
            if alist[i]:
                for j in range(i+i, n, i):
                    alist[j] = 0
        return sum(alist)-2
# @lc code=end

