#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A==B:
            return len(A) != len(set(A))
        first  = second = None
        for index in range(len(A)):
            if A[index] != B[index]:
                if first is not None and second is not None:
                    return False
                elif first is not None:
                    if A[first] == B[index] and B[first] == A[index]:
                        second = index
                        continue
                else:
                    first = index
        return bool(second)
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A==B:
            return len(A) != len(set(A))
        diffs = []
        for index in range(len(A)):
            if A[index] != B[index]:
                diffs.append(index)
        if len(diffs) != 2:
            return False
        i, j = diffs
        return A[i] == B[j] and B[i]==A[j]





# @lc code=end

