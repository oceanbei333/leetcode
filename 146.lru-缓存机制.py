#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
from typing import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.remain = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value


class DLinkedNode:
    def __init__(self, key: int = None, value: int = None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.remain = capacity
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            node.value = value
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                node = self.removeTail()
                self.cache.pop(node.key)
            node = DLinkedNode(key, value)
            self.addToHead(node)
            self.cache[key] = node

    def addToHead(self, node: DLinkedNode):
        prev = self.head
        next_ = self.head.next

        prev.next, next_.prev = node, node
        node.next, node.prev = next_, prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
