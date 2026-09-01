class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        l = set(nums)
        a = 0
        for i in l:
            if i < 0:
                a = a + 1
        if a == len(l):
            sum = max(l)
        else:
            for i in l:
                if i < 0:
                    pass
                else:
                    sum = sum + i
        return sum