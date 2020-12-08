#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        res = ''
        for s in bin(N)[2:]:
            res += str( int(s)^1 )
        return int(res, 2)
    def bitwiseComplement(self, N: int) -> int:
        return 2**(len(bin(N))-2) -1 -N
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1
        res = ''
        while N:
            res= str(( N%2 )^1) + res
            N >>= 1
        return int(res, 2)
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1
        res = ''
        while N:
            res= str(( N%2 )^1) + res
            N //= 2
        return int(res, 2)
# @lc code=end

