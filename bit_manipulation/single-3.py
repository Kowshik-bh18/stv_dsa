'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
'''

'''
Traverse the entire array, performing an XOR operation on all numbers. This will effectively cancel out all the numbers that appear twice, leaving us with the XOR of the two unique numbers.
Determine the rightmost set bit (bit that is 1) in the result from the first step. This set bit can be used to differentiate the two unique numbers since they must differ at this bit position.
Traverse the array again, but this time divide the numbers into two groups:
One group where the numbers have the rightmost set bit.
Another group where the numbers do not have this bit set.
Perform XOR operations while adding numbers in each group. This will cancel out the duplicate numbers, leaving only the unique numbers in each group.
Sort the two unique numbers in ascending order and return them.
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor,b1,b2 = 0,0,0
        for num in nums:
            xor^=num
        right_most_set_bit = xor & (-xor)
        for num in nums:
            if num&right_most_set_bit:
                b1^=num
            else:
                b2^=num
        return [b1,b2]
        