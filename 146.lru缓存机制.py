#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start

from collections import OrderedDict


class LinkNode(object):
    """
    docstring
    """

    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class DoubleLinkList(object):
    """
    docstring
    """

    def __init__(self):
        self.head = self.tail = LinkNode()

    def add_node(self, node: LinkNode):
        if self.head.next:
            self.head.next.pre = node
            node.next = self.head.next
        else:
            self.tail = node
        self.head.next, node.pre = node, self.head

    def get_node_by_key(self, key: int):
        node = self.head.next
        while node and node.key != key:
            node = node.next
        return node

    def delete_node(self, node: LinkNode):
        if node.next:
            node.next.pre = node.pre
        else:
            self.tail = node.pre
        node.pre.next = node.next


class LRUCache:

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('capacity must be positive!')
        self.capacity = capacity
        self.length = 0
        self.list = DoubleLinkList()

    def get(self, key: int) -> int:
        node = self.list.get_node_by_key(key)
        if node:
            self.list.delete_node(node)
            self.list.add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.list.get_node_by_key(key)
        if node:
            self.list.delete_node(node)
        else:
            self.length += 1
        self.list.add_node(LinkNode(key, value))
        if self.length > self.capacity:
            node = self.list.tail
            self.list.delete_node(node)
            self.length -= 1


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('capacity must be positive!')
        self.capacity = capacity
        self.length = 0
        self.list = DoubleLinkList()
        self.dict = dict()

    def get(self, key: int) -> int:
        node = self.dict.get(key)
        if node:
            self.list.delete_node(node)
            self.list.add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key)
        if node:
            self.list.delete_node(node)
        else:
            self.length += 1
        new_node = LinkNode(key, value)
        self.dict[key] = new_node
        self.list.add_node(new_node)
        if self.length > self.capacity:
            last_node = self.list.tail
            self.dict.pop(last_node.key)
            self.list.delete_node(last_node)
            self.length -= 1


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('capacity must be positive!')
        self.capacity = capacity
        self.length = 0
        self.dict = dict()

    def get(self, key: int) -> int:
        value = self.dict.get(key)
        if not value:
            return -1
        self.dict.pop(key)
        self.dict[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            self.length += 1
        self.dict[key] = value
        if self.length > self.capacity:
            key_first = list(self.dict.keys())[0]
            self.dict.pop(key_first)
            self.length -= 1

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end


def main():

    obj = LRUCache(2)
    assert -1 == obj.get(2)
    obj.put(1, 1)
    assert 1 == obj.get(1)
    obj.put(2, 1)
    obj.put(3, 1)
    assert -1 == obj.get(1)


if __name__ == "__main__":
    main()
