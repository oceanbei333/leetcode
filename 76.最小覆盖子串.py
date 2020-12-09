#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        length = len(s)
        l = r = 0
        res = ''
        counter_target = Counter()
        while r < length:
            while counter_t - counter_target and r < length:
                if s[r] in counter_target:
                    counter_target[s[r]] += 1
                else:
                    counter_target[s[r]] = 1
                r += 1
            if counter_t - counter_target:
                break
            while not counter_t - counter_target:
                l += 1
                counter_target[s[l-1]] -= 1
            if not res or len(res) > r-l:
                res = s[l-1:r]
        return res

    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        length = len(s)
        l = r = 0
        res = ''
        counter_target = Counter({c: 0 for c in s})
        for r in range(length):
            counter_target[s[r]] += 1
            if not counter_t - counter_target:
                while not counter_t - counter_target:
                    l += 1
                    counter_target[s[l-1]] -= 1
                if not res or len(res) > r-l+2:
                    res = s[l-1:r+1]
        return res

    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        need_count = len(t)
        l = 0
        res = ''
        for r in range(len(s)):
            if need[s[r]] > 0:
                need_count -= 1
            need[s[r]] -= 1
            if not need_count:
                while need[s[l]] < 0 :
                    need[s[l]] += 1
                    l += 1
                target = s[l:r+1]
                if not res or len(res) > len(target):
                    res = target
        return res
# @lc code=end
