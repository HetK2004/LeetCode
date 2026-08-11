class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = int(a,2) + int(b,2)
        s = str(bin(add))
        return s[2:]