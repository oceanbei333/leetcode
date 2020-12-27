#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def helper(dividend, divisor):
            res = 0
            while dividend >= divisor:
                cur = divisor  # 第一次是cur = divisor
                multiple = 1
                while cur+cur < dividend:
                    cur += cur   # 这里是将cur x 2，即直接比较divisor x 2的次方（加快比较速度）
                    multiple += multiple   # 保留divisor的倍数
                dividend -= cur    # dividend 变为 dividend-cur 进行下一轮while
                res += multiple
            return res
        res = helper(abs(dividend), abs(divisor))

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            res = - res

        MIN_INT, MAX_INT = -(1<<31), (1<<31)-1
        if res < MIN_INT:
            return MIN_INT
        elif res > MAX_INT:
            return MAX_INT
        else:
            return res
# @lc code=end
