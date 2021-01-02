#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [10001*n] * n
        dist[src] = 0
        pre = dist[:]
        for _ in range(K+1):
            for u, v, w in flights:
                dist[v] = min(dist[v], pre[u]+w)
            pre = dist[:]
        return dist[dst] if dist[dst] < 10001*n else -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        from collections import defaultdict
        from heapq import heappush, heappop
        graph = defaultdict(dict)
        best = defaultdict(lambda: float('inf'))
        for source, dest, cost in flights:
            graph[source][dest] = cost
        heap = [(0, 0, src)]
        while heap:
            cost, k, place = heappop(heap)
            if k > K+1 or cost > best[(k, place)]:
                continue
            if place == dst:
                return cost

            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best[(k+1, nei)]:
                    best[k+1, nei] = newcost
                    heappush(heap, (newcost, k+1, nei))
        return -1

# @lc code=end
