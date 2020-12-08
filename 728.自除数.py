#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            for num in str(n):
                if num == '0' or n%(int(num)):
                    break
            else:
                res.append(n)
        return res

        
# @lc code=end

