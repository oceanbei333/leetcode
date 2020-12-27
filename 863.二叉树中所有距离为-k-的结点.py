#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(root, parent=None):
            if not root:
                return
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root)
        res = []
        visited = set()
        queue = {(target, 0)}
        while queue:
            node, dist = queue.pop()
            if node and node not in visited:
                continue
            if dist == K:
                res.append(node.val)
                continue
            visited.add(node)
            queue.add((node.left, dist+1))
            queue.add((node.right, dist+1))
            queue.add((node.parent, dist+1))
        return res


# @lc code=end
