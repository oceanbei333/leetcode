#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        from collections import defaultdict
        adict = defaultdict(int)

        def dfs(root: TreeNode):
            if not root:
                return
            adict[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        max_c = max(adict.values())
        return [val for val, count in adict.items() if count == max_c]

    def findMode(self, root: TreeNode) -> List[int]:
        nums = []
        if not root:
            return nums

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)
        pre, count, max_, res = None, 0, 0, []
        for val in nums:
            if val == pre:
                count += 1
            else:
                pre = val
                count = 1
            if count == max_:
                res.append(val)
            elif count > max_:
                res = [val]
                max_ = count
        return res


# @lc code=end
