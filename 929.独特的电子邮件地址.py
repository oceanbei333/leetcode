#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        aset = set()
        for email in emails:
            pre, domain = email.split('@')
            aset.add( ( pre.split('+')[0].replace(".", ""), domain ) )
        return len(aset)
        
# @lc code=end

