#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root_val = postorder[-1]
        left_len = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:left_len], postorder[:left_len])
        root.right = self.buildTree(
            inorder[left_len+1:], postorder[left_len:len(postorder)-1])
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        indexes = {val: i for i, val in enumerate(inorder)}

        def _buildTree(i_l: int, i_r: int, p_l: int, p_r: int) -> TreeNode:
            if i_l > i_r:
                return
            i_root_index = indexes[postorder[p_r]]
            left_len = i_root_index-i_l
            root = TreeNode(postorder[p_r])
            root.left = _buildTree(i_l, i_l+left_len-1, p_l, p_l+left_len-1)
            root.right = _buildTree(i_l+left_len+1, i_r, p_l+left_len, p_r-1)
            return root
        return _buildTree(0, len(inorder)-1, 0, len(postorder)-1)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        head = TreeNode(postorder.pop())
        stack = [head]
        while postorder:
            node = TreeNode(postorder.pop())
            root = stack[-1]
            if root.val != inorder[-1]:
                root.right = node
            else:
                while stack and stack[-1].val == inorder[-1]:
                    root = stack.pop()
                    inorder.pop()
                root.left = node
            stack.append(node)
        return head

# @lc code=end
