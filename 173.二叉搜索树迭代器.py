#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.list = []
        self.preorder(root)

    def preorder(self, root):
        if not root:
            return
        self.preorder(root.right)
        self.list.append(root.val)
        self.preorder(root.left)

    def next(self) -> int:
        return self.list.pop()

    def hasNext(self) -> bool:
        return bool(self.list)


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.help(root)

    def help(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        self.help(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
