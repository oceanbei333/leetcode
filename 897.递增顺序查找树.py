#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        alist = []
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            alist.append(root)
            dfs(root.right)
        dfs(root)
        for index in range(len(alist)-1):
            alist[index].left = None
            alist[index].right =alist[index+1]
        return alist[0]
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = None
        self.node = None
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            if not self.node:
                self.node = root
                self.head = root
            else:
                self.node.left = None
                self.node.right = root
                self.node = root
            dfs(root.right)
        dfs(root)
        return self.head
# @lc code=end

