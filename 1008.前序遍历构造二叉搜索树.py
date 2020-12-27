#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        indexes = {val: index for index, val in enumerate(inorder)}

        def dfs(p_l, p_r, i_l, i_r):
            if p_l > p_r:
                return
            root = TreeNode(preorder[p_l])
            left_len = indexes[root.val] - i_l
            root.left = dfs(p_l+1, p_l+left_len, i_l, i_l+left_len-1)
            root.right = dfs(p_l+left_len+1, p_r, i_l+left_len+1, i_r)
            return root
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        head = TreeNode(preorder[0])
        stack = [head]
        for val in preorder[1:]:
            node = TreeNode(val)
            root = stack[-1]
            while stack and stack[-1].val < node.val:
                root = stack.pop()
            if root.val > node.val:
                root.left = node
            else:
                root.right = node
            stack.append(node)
        return head
# @lc code=end
