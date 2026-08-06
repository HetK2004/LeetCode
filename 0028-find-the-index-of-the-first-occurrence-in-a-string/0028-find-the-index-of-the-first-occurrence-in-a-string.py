class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = needle[0]
        b = len(needle)
        offset = 0
        while a in haystack:
            c = haystack.find(a)
            if needle == haystack[c:c+b] :
                return offset + c
            else:
                haystack = haystack[c+1::]
                offset += c + 1
        else :
            return -1