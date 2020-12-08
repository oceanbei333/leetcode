#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        total = 0
        for i in range(1,length+1, 2):
            for j in range(length):
                if j+i > length:
                    break
                total += sum(arr[j:j+i])
        return total

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        return sum(
            sum(arr[j:j+i])
            for i in range(1,length+1, 2)
            for j in range(length-i+1)
        )

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        for index in range(1, length):
            arr[index]+=arr[index-1]
        total = 0
        for i in range(1,length+1, 2):
            for j in range(length-i+1):
                if not j:
                    total += arr[i-1]
                else:
                    total+= arr[j+i-1]-arr[j-1]
        return total

# @lc code=end

