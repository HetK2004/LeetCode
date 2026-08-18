class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        right = len(nums)//2
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[right+i])
        return l