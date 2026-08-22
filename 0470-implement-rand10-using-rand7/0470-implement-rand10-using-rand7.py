class Solution:
    def rand10(self):
        while True:
            n = (rand7()-1) * 7 + rand7()
            if n <= 40:
                return (n - 1) % 10 + 1