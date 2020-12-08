#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False]*1000000


    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.set[key]

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False]


    def add(self, key: int) -> None:
        if len(self.set) < key+1:
            self.set.extend([False]*(key+1-len(self.set)))
        self.set[key] = True
        

    def remove(self, key: int) -> None:
        if len(self.set) >= key+1:
            self.set[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if len(self.set) >= key+1:
            return self.set[key]
        else:
            return False




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

