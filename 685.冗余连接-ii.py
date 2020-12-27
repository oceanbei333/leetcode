#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        f = dict()

        def find(x: int) -> int:
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x: int, y: int):
            f[find(x)] = f[find(y)]

        graph = dict()
        ans = None
        for u, v in edges:
            if v in graph:
                # 找到冲突边，不要加入到图中
                ans = (u, v)
                continue
            if find(u) == find(v) and not ans:
                # 找到环
                ans = (u, v)
            union(u, v)
            graph[v] = u
        if len({find(point) for point in range(1, len(edges)+1)}) == 1:
            # 如果当前没有环
            return ans
        else:
            # 根据入度找到另外一条边
            return graph[ans[1]], ans[1]

# @lc code=end
