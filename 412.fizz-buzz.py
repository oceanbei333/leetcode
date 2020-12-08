#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
from typing import Iterator


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def func(n:int)-> Iterator:
            for i in range(1,n+1):
                if not i%3 and not i%5:
                    yield "FizzBuzz"
                elif not i%3:
                    yield "Fizz"
                elif not i%5:
                    yield "Buzz"
                else:
                    yield str(i)
        return list(func(n))
        
# @lc code=end

