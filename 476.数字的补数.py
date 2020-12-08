#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num))-2) -1 -num
    def findComplement(self, num: int) -> int:
        return num^(int('1'*( len(bin(num))-2 ), 2))
    def findComplement(self, num: int) -> int:
        return int(''.join('1' if i=='0' else '0' for i in bin(num)[2:]), 2)

# @lc code=end

