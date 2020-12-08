#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [-1]*1000000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.map[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.map[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.map[key] = -1
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [-1]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if len(self.map) < key+1:
            self.map.extend([-1]*(key+1-len(self.map)))
        self.map[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if len(self.map) >= key+1:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if len(self.map) >= key+1:
            self.map[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

