class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        s = (arr[0] - arr[1]) * -1
        l = len(arr)
        i = 0
        j = 1
        c = 0
        while i < l-1 :
            a = (arr[i] - arr[j]) * -1
            if a == s :
                c = 1
            else:
                c = 0
                break
            j += 1
            i += 1
        if c == 0:
            return False
        else:
            return True
