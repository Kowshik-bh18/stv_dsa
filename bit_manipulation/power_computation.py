class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        result = 1
        while m>0:
            if m%2==1:
                result = result*x
            x = x*x
            m//=2
        if n>0:
            return result
        return 1/result

"it is based on rewriting exponent in even and reduce by half each time"