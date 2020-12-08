#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        def find_val(node:TreeNode, root:TreeNode, alist:list):
            alist.append(root)
            if root is node:
               return
            if root.val > node.val:
                find_val(node, root.left, alist)
            if root.val < node.val:
                find_val(node, root.right, alist)
        p_list  = []
        q_list  = []
        find_val(p, root, p_list)
        find_val(q, root, q_list)
        length = min(len(p_list), len(q_list))
        for index in range(length):
            if p_list[index] is not q_list[index]:
                return p_list[index-1]
        return q_list[length-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_val(node:TreeNode, root:TreeNode)->list:
            alist = []
            while root:
                alist.append(root)
                if root is node:
                    break
                if root.val > node.val:
                    root = root.left
                else:
                    root = root.right
            return alist
        p_list = find_val(p, root)
        q_list = find_val(q, root)
        ancestor = p_list[0]
        for node1, node2 in zip(p_list, q_list):
            if node1 is node2:
                ancestor = node1
            else:
                break
        return ancestor
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root is p or root is q:
                return root
            if root.val > p.val and root.val >q.val:
                root = root.left
            elif root.val < p.val and root.val <q.val:
                root = root.right
            else:
                return root

# @lc code=end

