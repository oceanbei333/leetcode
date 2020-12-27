#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(p_l: int, p_r: int, i_l: int, i_r: int):
            if p_l > p_r:
                return None

            # 前序遍历中的第一个节点就是根节点
            p_root_index = p_l
            # 在中序遍历中定位根节点
            i_root_index = index[preorder[p_root_index]]

            # 先把根节点建立出来
            root = TreeNode(preorder[p_root_index])
            # 得到左子树中的节点数目
            left_len = i_root_index - i_l
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(
                p_l + 1, p_l + left_len, i_l, i_root_index - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(
                p_l + left_len + 1, p_r, i_root_index + 1, i_r)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        # 在中序遍历中定位根节点, 也可以得到左右子树的长度
        left_len = inorder.index(preorder[0])

        # 先把根节点建立出来
        root = TreeNode(preorder[0])
        # 得到左子树中的节点数目
        root.left = self.buildTree(
            preorder[1: 1+left_len],
            inorder[:left_len]
        )
        root.right = self.buildTree(
            preorder[1+left_len:],
            inorder[left_len + 1:]
        )
        return root

    def buildTree(self, prerder: List[int], inorder: List[int]) -> TreeNode:
        if not prerder:
            return
        head = TreeNode(prerder[0])
        stack = [head]
        inorder_reverse = inorder[::-1]
        for val in prerder[1:]:
            child = TreeNode(val)
            root = stack[-1]
            if root.val !=inorder_reverse[-1]:
                root.left = child
            else:
                while stack and stack[-1].val == inorder_reverse[-1]:
                    root = stack.pop()
                    inorder_reverse.pop()
                root.right = child
            stack.append(child)
        return head


# @lc code=end
