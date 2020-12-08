#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
from typing import no_type_check


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        length = 10
        def get_time(s:str)->str:
            hour = str(get_number(s[:4]))
            mins = str(get_number(s[4:]))
            if len(mins) == 1:
                mins = f"0{mins}"
            return hour + ":" + mins
        def get_number(s:str)->int:
            if not s:
                return 0
            return int( f"0b{s}",2)
        def func(leds:str):
            if len(leds)== length:
                if get_number(leds[:4])> 11:
                    return
                if get_number(leds[4:])>59:
                    return
                if leds.count('1') == num:
                    result.append(get_time(leds))
                return
            func(leds+'0')
            func(leds+'1')
        func('')
        return result

    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        length = 10
        def get_time(s:str)->str:
            hour = str(get_number(s[:4]))
            mins = str(get_number(s[4:]))
            if len(mins) == 1:
                mins = f"0{mins}"
            return hour + ":" + mins
        def get_number(s:str)->int:
            if not s:
                return 0
            return int( f"0b{s}",2)
        def func(leds:str):
            if len(leds)==4 and get_number(leds[:4])> 11:
                    return
            if len(leds)== length:
                if get_number(leds[4:])>59:
                    return
                if leds.count('1') == num:
                    result.append(get_time(leds))
                return
            func(leds+'0')
            func(leds+'1')
        func('')
        return result


        
# @lc code=end

