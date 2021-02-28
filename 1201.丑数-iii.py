#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            if x%y == 0:
                return y
            return gcd(y, x%y)

        def lcm(x, y):
            return x*y//gcd(x,y)

        l = min(a,b,c)
        r = min(int(2*pow(10, 9)+1), l*n)
        lcm_ab, lcm_ac, lcm_bc, lcm_abc = lcm(a,b), lcm(a,c), lcm(b,c), lcm(lcm(a,b), c)

        while l<r:
            mid = l+(r-l)//2
            N = mid//a+mid//b+mid//c-mid//lcm_ab-mid//lcm_ac-mid//lcm_bc+mid//lcm_abc
            if N<n:
                l = mid+1
            else:
                r = mid
        return l
# @lc code=end
