#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        alist = []
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            alist.append(root.val)
            dfs(root.right)
        dfs(root)
        v_min = alist[1] -alist[0]
        for index in range(2,len(alist)):
            v_min = min(v_min, alist[index]-alist[index-1])
        return v_min
    def minDiffInBST(self, root: TreeNode) -> int:
        self.alist = []
        self.min = float('inf')
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            if self.alist:
                self.min = min(self.min, root.val - self.alist[-1])
            self.alist.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.min


# @lc code=end

