#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)
        queue = [('JFK', ['JFK'])]
        visited = set()
        result = []
        while queue:
            new_queue = []
            queue.sort()
            result.append(queue[0])
            for source, path in queue:
                visited.add(source)
                for dest in graph[source]:
                    if dest not in visited:
                        new_queue.append([dest, path+[dest]])
            queue = new_queue
        return result

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)

        def dfs(curr: str):
            # 按照优先级，顺序遍历目的地
            graph[curr].sort(reverse=True)
            while graph[curr]:
                dfs(graph[curr].pop())
            stack.append(curr)

        for source, dest in tickets:
            graph[source].append(dest)

        stack = list()
        dfs("JFK")
        return stack[::-1]

# @lc code=end
