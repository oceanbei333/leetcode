#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        adict = dict()
        def dfs(root: 'TreeNode'):
            if root.left:
                adict[root.left.val] = root
                dfs(root.left)
            if root.right:
                adict[root.right.val] = root
                dfs(root.right)
        def get_path(root:"TreeNode"):
            res = [root]
            while adict.get(root.val):
                res.append(adict[root.val])
                root = res[-1]
            return res[::-1]
        dfs(root)
        path1 = get_path(p)
        path2 = get_path(q)
        for index in range(len(path1)):
            if path1[index] is p  and path2[index] is p:
                return p
            elif path1[index] is q  and path2[index] is q:
                return q
            if path1[index] is not path2[index]:
                return path1[index-1]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        adict = dict()
        def dfs(root: 'TreeNode'):
            if root.left:
                adict[root.left.val] = root
                dfs(root.left)
            if root.right:
                adict[root.right.val] = root
                dfs(root.right)
        def get_path(root:"TreeNode"):
            res = [root]
            while adict.get(res[-1].val):
                res.append(adict[res[-1].val])
            return res
        dfs(root)
        path1 = get_path(p)
        path2 = get_path(q)
        for index in range(len(path1)):
            index = -index -1
            if path1[index] is p  and path2[index] is p:
                return p
            elif path1[index] is q  and path2[index] is q:
                return q
            if path1[index] is not path2[index]:
                return path1[index+1]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root or root is p or root is q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if not all((left, right)):
                return left or right
            return root
        return dfs(root)

# @lc code=end

