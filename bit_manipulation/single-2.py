'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #bitwise-approach
        # ans = 0
        # for bitindex in range(32):
        #     count = 0
        #     for i in range(len(nums)):
        #         if nums[i] & (1<<bitindex):
        #             count+=1
        #     if count%3:
        #         ans |=(1<<bitindex)

        # if ans>=2**31:
        #     ans-=2**32
        # return ans

        #sorting_approach
        # nums.sort()
        # for i in range(1,len(nums),3):
        #     if nums[i]!=nums[i-1]:
        #         return nums[i-1]
        # return nums[len(nums)-1]

        #ptimized bit approach

        ones = 0
        twos = 0
        for num in nums:
            ones = (ones^num) & (~twos)
            twos = (twos^num) & (~ones)
        return ones

            
        