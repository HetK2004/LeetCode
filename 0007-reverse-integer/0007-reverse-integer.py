class Solution:
	def reverse(self, x: int) -> int:
		v = 0
		if x < 0:
			n = str(x)
			n = n[::-1].replace("-","")
			if len(n) >= 10:
				if int(n) > (2**31-1):
					v = 0
				else:
					v = -int(n)
			else:
				v = -int(n)
		else:
			n = str(x)
			n = n[::-1]
			if len(n) >= 10:
				if int(n) > (2**31) :
					v = 0
				else:
					v = int(n)
			else:
				v = int(n)
		return v
s = Solution()
x = int()
print(s.reverse(x))