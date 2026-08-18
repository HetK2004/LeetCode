class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        m = 0
        while left < len(nums):
            if nums[left] == 1:
                right = left
                count = 0
                
                while right < len(nums) and nums[right] == 1:
                    count = count + 1
                    right = right + 1
                
                m = max(m,count)
                left = right
            else:
                left = left + 1
        return m