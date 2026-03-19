'''
The naive method tries every number, which is slow when n is large. But our possible answer space (from 1 to n) is sorted, meaning if a certain number squared is less than or equal to n, then all smaller numbers will also work. This allows us to apply Binary Search on the answer space to efficiently find the largest number whose square is less than or equal to n.
First, note that the answer lies between 1 and the given number n.
Set the search range with the smallest value as 1 and the largest value as n.
Use binary search within this range to test possible numbers.
At each step, take the middle number and check if its square is less than or equal to n.
If it is, record this number as a candidate and move right to check for a larger number.
If the square is greater than n, move left to check smaller numbers.
Continue this process until the range closes, and the largest recorded number will be the square root.
'''

#Note:- we can directly return 'high' becuase it will be in correct position when we stop because it tries to move towards solution
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        if x<2:
            return x
        while(low<=high):
            mid = (low+high)//2
            if (mid*mid <=x):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans
        