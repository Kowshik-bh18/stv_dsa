'''
Intuition
We are going to use the Binary Search algorithm to optimize the approach.

Approach
First, check if the number of elements is already greater than the allowed limit. If so, no answer is possible, so return -1.
Then, identify the largest number in the list.
Start with two markers , one at the smallest possible number (1), and another at the largest number in the list.
Use a loop to narrow down the range. In each step, find the number that is in the middle of the current range.
Check if using this middle number as a divisor results in a total that is within the allowed limit. This is done using a helper that adds up the rounded-up results of each division.
If the result is within the allowed limit, it means this number might work, but a smaller one could be better. So, look in the lower half of the current range.
If the result is too large, it means this number is too small. So, look in the upper half of the range instead.
Repeat this process until the range closes. The smallest number that works will be pointed to by the left marker, and that's the answer.

'''

from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def tot_sum(i):
            sumi = 0
            for num in nums:
                sumi+=math.ceil(num/i)
            return sumi<=threshold
        
        left = 1
        right = max(nums)
        while(left<=right):
            mid = (left+right)//2
            val = tot_sum(mid)

            if val:
                ans = mid 
                right = mid-1
            else:
                left = mid+1
        return ans

        