class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal) :
            for i in range(len(s)):
                a = s[i:] + s[:i]
                if a == goal:
                    return True
            else :
                return False
        else :
            return False