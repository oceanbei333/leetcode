#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sub = [0]
        for num in nums:
            sub.append(sub[-1]+num)

        @functools.lru_cache(None)
        def dp(i: int, m: int) -> int:
            if not m and not i:
                return 0
            if i < m or not m:
                return float('inf')
            res = float('inf')
            for k in range(i):
                res = min(res, max(dp(k, m-1), sub[i] - sub[k]))
            return res
        return dp(len(nums), m)


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end
