class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            n=abs(n)
            if n == 0:
                return 1
            elif n % 2 == 0:
                return pow(x*x, n// 2)
            else:
                return x*pow(x*x,(n-1)//2)
        return float(pow(x,n)) if n >= 0 else 1/pow(x,n)
