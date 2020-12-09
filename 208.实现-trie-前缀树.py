#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
from collections import defaultdict
from typing import List
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        trie = lambda: defaultdict(trie)
        def trie():
            return defaultdict(trie)
        self.trie = trie()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        child = self.trie
        for c in word:
            child = child[c]
        child['is_word'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        child = self.trie
        for c in word:
            if c in child:
                child = child[c]
            else:
                return False
        return child.get('is_word', False)


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        child = self.trie
        for c in prefix:
            if c in child:
                child = child[c]
            else:
                return False
        return True
class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie =  TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        child = self.trie
        for c in word:
            child = child.children[c]
        child.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        child = self.trie
        for c in word:
            if c in child.children:
                child = child.children[c]
            else:
                return False
        return child.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        child = self.trie
        for c in prefix:
            if c in child.children:
                child = child.children[c]
            else:
                return False
        return True

class TrieNode:
    def __init__(self, val=None, children:List=[], is_word=False) -> None:
        self.val = val
        self.is_word = is_word
        self.children = {node.val:node for node in children}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root =  TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]
        root.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return root.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for c in prefix:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

