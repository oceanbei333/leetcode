#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def _inorderTraversal(root:TreeNode):
            if not root:
                return
            _inorderTraversal(root.left)
            res.append(root.val)
            _inorderTraversal(root.right)
        _inorderTraversal(root)
        return res
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

        
# @lc code=end

