class Solution:
    def cal(self, n : int ):
        li = []
        while n > 0:
            li.append((n%10)**2)
            n = n // 10
        return sum(li)
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = self.cal(n)
        return True