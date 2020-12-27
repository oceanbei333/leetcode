#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(node_a, node_b):
            node = head = ListNode()
            while node_a and node_b:
                if node_a.val < node_b.val:
                    node.next, node_a = node_a, node_a.next
                else:
                    node.next, node_b = node_b, node_b.next
                node = node.next
            node.next = node_a or node_b
            return head.next
        return reduce(merge, lists) if lists else None

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        head = node = ListNode()
        heap, n = [], len(lists)
        for i in range(n):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        while heap:
            _, index = heappop(heap)
            node.next = lists[index]
            node = node.next
            next_ = lists[index].next
            lists[index] = next_
            if next_:
                heappush(heap, (next_.val, index))
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        if not lists:
            return
        head = node = ListNode()
        heap = []
        for list_ in lists:
            if list_:
                heappush(heap, (list_.val, id(list_), list_))
        while heap:
            *_, min_node = heappop(heap)
            node.next, min_node = min_node, min_node.next
            node = node.next
            if min_node:
                heappush(heap, (min_node.val, id(node), min_node))
        return head.next


# @lc code=end
