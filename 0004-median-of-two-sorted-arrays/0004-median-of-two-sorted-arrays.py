class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2

        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] > l[j]:
                    a = l[i]
                    l[i] = l[j]
                    l[j] = a

        if len(l)%2!=0:
            v = (len(l)//2)
            s = l[v]
        else:
            s1 = (len(l)//2)
            s2 = (len(l)//2)-1
            s = (l[s1] + l[s2])/2
        return s