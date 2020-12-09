#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        self.res = 0

        def dp(i: int, absent_n: int, late_n: int):
            if i == n:
                self.res += 1
                return
            # late
            if late_n < 2:
                dp(i+1, absent_n, late_n+1)
            # absent
            if not absent_n:
                dp(i+1, 1, 0)
            # present
            dp(i+1, absent_n, 0)
        dp(0, 0, 0)
        return self.res

    def checkRecord(self, n: int) -> int:
        dp = [[]for _ in range(n+1)]
        dp[0].append((0, 0))
        for i in range(n):
            for absent_n, late_n in dp[i]:
                if late_n < 2:
                    dp[i+1].append((absent_n, late_n+1))
                if not absent_n:
                    dp[i+1].append((1, 0))
                dp[i+1].append((absent_n, 0))
        return len(dp[-1])

    def checkRecord(self, n: int) -> int:
        '''
        第一个数字表示缺席次数，第二个数字表示迟到次数
        '''
        dp = [[0, 0] for _ in range(3)]
        dp[0][0] = 1
        max_ = 1000000007
        for _ in range(n):
            dp[0][0], dp[1][0], dp[2][0], dp[0][1], dp[1][1], dp[2][1] = (
                (dp[0][0]+dp[1][0]+dp[2][0]) % max_, dp[0][0], dp[1][0],
                (dp[0][0]+dp[1][0]+dp[2][0]+dp[0][1]+dp[1]
                 [1]+dp[2][1]) % max_, dp[0][1], dp[1][1]
            )
        return (dp[0][0] + dp[1][0] + dp[2][0] + dp[0][1] + dp[1][1] + dp[2][1]) % max_

    def checkRecord(self, n: int) -> int:
        '''
        第一个数字表示缺席次数，第二个数字表示迟到次数
        '''
        _00, _01, _02, _10, _11, _12 = 1, 0, 0, 0, 0, 0
        max_ = 1000000007
        for _ in range(n):
            _00, _01, _02, _10, _11, _12 = (
                (_00+_01+_02) % max_, _00, _01,
                (_00+_01+_02+_10+_11+_12) % max_, _10, _11
            )
        return (_00 + _01 + _02 + _10 + _11 + _12) % max_
# @lc code=end
