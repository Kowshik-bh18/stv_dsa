'''You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.



A number which completely divides another number is called it's divisor.


Example 1

Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.

Example 2

Input: n = 8

Output: [1, 2, 4, 8]

Explanation: The divisors of 8 are 1, 2, 4, 8.
'''

class Solution:
    def divisors(self, n):
        res = []
        for i in range(1,n+1):
            if n%i==0:
                res.append(i)
        return res

'''
if they only asked to print divisor then we can optimize above with sqrt(n) time complexity

We can optimise the previous approach by using the property that for any non-negative integer n, 
if d is a divisor of n then n/d is also a divisor of n. 
This property is symmetric about the square root of N. 
Thus, by traversing just the first half we can avoid redundant iteration 
and computations improving the efficiency of the algorithm.
'''
import math
class Solution:
    def divisors(self, n):
        res = []
        for i in range(1,int(math.sqrt(n)+1)):
            if n%i==0:
                res.append(i)
                if (n//i!=0): #-> because it should not be same number ex:- 6 6
                    res.append(n//i)
        res.sort()
        return res
