#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        from collections import defaultdict
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[1]].add(edge[0])
            graph[edge[0]].add(edge[1])
        queue = [i for i in range(n) if len(graph[i]) == 1]
        while True:
            new_queue = []
            for root in queue:
                for next_ in graph[root]:
                    graph[next_].remove(root)
                    if len(graph[next_]) == 1:
                        new_queue.append(next_)
            if new_queue:
                queue = new_queue
            else:
                return queue

# @lc code=end
