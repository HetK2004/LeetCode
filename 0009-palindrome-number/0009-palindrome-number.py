class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x > 0:
            a = str(x)
            if a == a[::-1]:
                return True
            else:
                return False
        else:
            return True