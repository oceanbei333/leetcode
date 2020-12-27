#
# @lc app=leetcode.cn id=818 lang=python3
#
# [818] 赛车
#

# @lc code=start
class Solution:
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            # k 是第一个超过t的步数
            k = t.bit_length()
            # 如果只前进就可以到达
            if t == 2**k - 1:
                dp[t] = k
                continue
            # 如果前进了k-1次, 也就是没有超过终点
            dis_front = 2**(k-1) - 1
            for j in range(k - 1):
                # 如果后退了 j 次
                dis_back = 2**j-1
                # 需要两次转向，因为，最后肯定是要朝向终点的
                steps = k-1+j + 2
                dp[t] = min(dp[t], dp[t - (dis_front-dis_back)] + steps)
            # 如果前进了k次, 也就是超过终点, 并且不能超过太多
            dis_front = 2**k - 1
            if dis_front - t < t:
                # 需要转向一次，因为超过之后，然后转向
                steps = k + 1
                dp[t] = min(dp[t], dp[dis_front-t] + steps)
        return dp[target]

    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0
        import heapq

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps:
                continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1  # No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]
