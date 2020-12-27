#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        graph = defaultdict(list)
        dist = defaultdict(lambda: float('inf'))
        unvisited = {node for node in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        dist[K] = 0
        while unvisited:
            # 从没有访问的结点中，找到一个距离最近的结点，第一次的话就是K结点
            node = min((node for node in unvisited),
                       key=lambda node: dist[node])
            unvisited.remove(node)
            # 更新所有邻居的距离
            for next_, d in graph[node]:
                dist[next_] = min(dist[next_], dist[node] + d)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        from heapq import heappush, heappop
        graph = defaultdict(list)
        dist = dict()
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, K)]

        while heap:
            d, node = heappop(heap)
            if node in dist:
                continue
            # 没有访问的结点中，最短距离的结点就是其最终最短距离
            dist[node] = d
            for nei, d2 in graph[node]:
                heappush(heap, (d+d2, nei))
        return max(dist.values()) if len(dist) == N else -1

    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        graph = defaultdict(list)
        dist = {node: float('inf') for node in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((w, v))

        def dfs(node, d):
            if d >= dist[node]:
                return
            dist[node] = d
            for t, nei in sorted(graph[node]):
                dfs(nei, d+t)
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


# @lc code=end
