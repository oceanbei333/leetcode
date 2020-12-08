#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        for _ in range(k):
            last = nums[-1]
            for index in range(len(nums)-1, 0, -1):
                nums[index] = nums[index-1]
            nums[0] = last
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:]=nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        if not k:
            return nums
        nums[:]=nums[::-1]
        nums[:k] = nums[k-1::-1]
        nums[k:] = nums[-1:k-1:-1]
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k%length
        start = -1
        count = 0
        while k and count < length:
            start += 1
            pre = nums[start]
            nxt = (start+k)%length
            while nxt != start:
                nums[nxt], pre = pre, nums[nxt] 
                count += 1
                nxt = (nxt+k)%length
            nums[nxt] = pre
            count+=1
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k%length
        start = count = 0
        while k and count < length:
            pre = nums[start]
            nxt = start
            while True:
                nxt = (nxt+k)%length
                nums[nxt], pre = pre, nums[nxt] 
                count += 1
                if nxt == start:
                    break
            start += 1
# @lc code=end

