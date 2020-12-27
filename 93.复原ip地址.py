#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        ips = ['']*4

        def dfs(count: int, index: int):
            if count == 4 and index == n:
                res.append('.'.join(ips))
            if index == n or count ==4:
                return
            if s[index] == '0':
                ips[count] = '0'
                dfs(count+1, index+1)
            for i in range(index, n):
                if 0 < int(s[index:i+1]) <= 255:
                    ips[count] = s[index:i+1]
                    dfs(count+1, i+1)
                else:
                    break
        dfs(0, 0)
        return res


# @lc code=end
