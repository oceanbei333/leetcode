#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
import string


class Solution:
    letters = string.ascii_letters
    numbers = string.digits

    def isPalindrome(self, s: str) -> bool:
        s_with_letters = self.get_letters()
        new_s = []
        for i in s:
            if self.is_letters_or_numbers(i):
                new_s.append(i)
        start = 0
        end = len(new_s) - 1
        while start < end:
            if new_s[start].lower() != new_s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def get_letters(self, s: str) -> bool:
        return

    def is_letters_or_numbers(self, s: str):
        return s in self.letters or s in self.numbers
        # @lc code=end
