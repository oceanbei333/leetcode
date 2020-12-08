#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        aset = set()
        for i in range(2, n):
            if  not any(not i%num for num in aset):
                aset.add(i)
        return len(aset)

# @lc code=end

