import math
class Solution:
    def fib(self, n: int) -> int:
        r = 1.618034
        s = -0.618034
        f = (math.pow(r,n) - math.pow(s,n))/sqrt(5)
        f = round(f)
        return f
