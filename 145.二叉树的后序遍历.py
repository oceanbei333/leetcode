#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        dfs(root)
        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == pre:
                res.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res, visited = [], [], {None}
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.right in visited:
                res.append(root.val)
                visited.add(root)
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        return res[::-1]


# @lc code=end
