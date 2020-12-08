#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
from time import sleep
class Foo:
    def __init__(self):
        self.is_first_finished = False
        self.is_second_finished = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.is_first_finished = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while not self.is_first_finished:
            sleep(0.1)
        printSecond()
        self.is_second_finished = True
            


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while not self.is_second_finished:
            sleep(0.1)
        printThird()
from threading import Lock
class Foo:
    def __init__(self):
        self.first_lock = Lock()
        self.second_lock = Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_lock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.first_lock:
            printSecond()
            self.second_lock.release()
            


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.second_lock:
            printThird()



# @lc code=end

