class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = list(set(nums))
        l = []
        for i in a:
            l.append(nums.count(i))
        b = l.index(max(l))
        return a[b]