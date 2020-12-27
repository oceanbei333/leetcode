#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        # 0, n-1的阶乘
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = ''
        valid = [1] * n
        for i in range(1, n + 1):
            order = k // factorial[- i] + 1
            for j in range(1, n + 1):
                order -= valid[j-1]
                if not order:
                    # j就是首位
                    ans += str(j)
                    valid[j-1] = 0
                    break
            k %= factorial[-i]
        return ans

    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        # 0, n-1的阶乘
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        k -= 1
        ans = ''
        nums = list(range(1, n+1))
        for i in range(1, n + 1):
            order = k // factorial[- i]
            ans += str(nums[order])
            nums.remove(nums[order])
            k %= factorial[-i]
        return ans


# @lc code=end
