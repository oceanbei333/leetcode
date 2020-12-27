#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        left_len = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(
            pre[1:1+left_len], post[:left_len])
        root.right = self.constructFromPrePost(
            pre[1+left_len:], post[left_len:len(post)-1])
        return root

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        indexes = {val: index for index, val in enumerate(post)}

        def _func(p_l, p_r, pt_l, pt_r):
            if p_l > p_r:
                return
            root = TreeNode(pre[p_l])
            if p_l == p_r:
                return root
            left_len = indexes[pre[p_l+1]]-pt_l + 1
            root.left = _func(p_l+1, p_l+left_len, pt_l, pt_l+left_len-1)
            root.right = _func(p_l+1+left_len, p_r, pt_l+left_len, pt_r-1)
            return root
        return _func(0, len(pre)-1, 0, len(post)-1)

# @lc code=end
