class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
        else :
            a = 0
            for i in nums:
                if target >= i :
                    a += 1
            return a
             