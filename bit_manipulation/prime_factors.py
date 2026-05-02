class Solution:
    def primeFactors(self, queries):
        #your code goes here
        out = []
        for n in queries:
            out.append(self.generate(n))
        return out
            
    def generate(self,n):
        res = []
        for i in range(2,n+1):
            if n%i==0:
                while n%i==0:
                    res.append(i)
                    n//=i
        return res
ans = Solution()
print(ans.primeFactors( [7, 12, 18]))



#optmized approach


import math

def prime_factors(n):
    factors = []

    # Step 1: Handle factor 2 separately (optimization)
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Step 2: Check only odd numbers from 3 to √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Step 3: If n > 1, it's a prime
    if n > 1:
        factors.append(n)

    return factors


# Example usage
n = 36
print(prime_factors(n))   # Output: [2, 2, 3, 3]

n = 37
print(prime_factors(n))   # Output: [37]
