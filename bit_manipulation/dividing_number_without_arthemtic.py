'''
Divide two integers without using multiplication, division and mod operator

Problem Statement: Given the two integers, dividend and divisor. Divide without using the mod, division, or multiplication operators and return the quotient.

The fractional portion of the integer division should be lost as it truncates toward zero.

As an illustration, 8.345 and -2.7335 would be reduced to 8 and -2 respectively.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        #brute force
        # def div(a,b):
        #     count = 0
        #     sumi =0
        #     while(sumi+b<=a):
        #         sumi+=b
        #         count+=1
        #     return count
        # res = div(abs(dividend),abs(divisor))
        # if divisor>0 and dividend>0:
        #     return res
        # elif divisor<0 and dividend<0:
        #     return res
        # else:
        #     return -1*res

        #optimal

        sign = True
        if (dividend>=0 and divisor<0) or (dividend<0 and divisor>=0):
            sign=False
        a,b = abs(dividend),abs(divisor)

        quotient = 0

        while a>=b:
            count = 0
            while a>=(b<<(count+1)):
                count+=1
            a-=(b<<count)
            quotient+=(1<<(count))
        
        if quotient>=(1<<31):
            return (1<<31)-1 if sign else -(1<<31)
        return quotient if sign else -quotient


'''
Determine the sign of the final result by checking if the dividend and divisor have opposite signs.
Convert both numbers to positive using their absolute values to simplify the logic.
To speed up division, subtract powers of two multiples of the divisor instead of subtracting it one by one.
Use bit shifting to efficiently find the largest multiple of the divisor that fits into the remaining dividend.
Subtract this multiple from the dividend and accumulate the equivalent power of two into the result.
Repeat until the dividend becomes smaller than the divisor.
Clamp the result to 32-bit signed integer limits if necessary to prevent overflow.
Apply the correct sign to the result and return the final quotient.


Time Complexity: O((logN)^2) – (where N is the absolute value of dividend). The outer loop runs for O(logN) times. The inner loop runs for O(logN) (approx.) times as well.
Space Complexity: O(1) – Using a couple of variables i.e., constant space.

'''


       
        