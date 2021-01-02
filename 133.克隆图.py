#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val)

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # 将题目给定的节点添加到队列
        queue = [node]
        # 克隆第一个节点并存储到哈希表中
        visited = dict()
        visited[node] = Node(node.val)

        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            new_queue = []
            for n in queue:
                # 遍历该节点的邻居
                for nei in n.neighbors:
                    if nei not in visited:
                        # 如果没有被访问过，就克隆并存储在哈希表中
                        visited[nei] = Node(nei.val, [])
                        # 将邻居节点加入队列中
                        new_queue.append(nei)
                    # 更新当前节点的邻居列表
                    visited[n].neighbors.append(visited[nei])
            queue = new_queue

        return visited[node]

# @lc code=end
