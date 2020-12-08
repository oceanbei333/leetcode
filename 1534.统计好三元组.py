#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    total += all(( abs(arr[i] - arr[j]) <= a, abs(arr[j] - arr[k]) <= b, abs(arr[i] - arr[k]) <= c ))
        return total
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(all(( abs(arr[i] - arr[j]) <= a, abs(arr[j] - arr[k]) <= b, abs(arr[i] - arr[k]) <= c ))
        for i in range(len(arr))
            for j in range(i+1, len(arr))
                for k in range(j+1, len(arr)))
                    
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                print(j, k)
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
                        if ans:
                            print(j, k, l, r, ans, total[r], total[l-1])
                            break
            for k in range(arr[j], 1001):
                total[k] += 1
        
        # return ans


# @lc code=end

