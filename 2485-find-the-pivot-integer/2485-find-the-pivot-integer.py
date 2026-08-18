import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        b = math.sqrt((n * (n + 1))/2)
        if b % 1 == 0.0 :
            return int(b)
        else:
            return -1
