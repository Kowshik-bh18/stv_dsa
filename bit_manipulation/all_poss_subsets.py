'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(1<<len(nums)):
            mini_sub = []
            for j in range(len(nums)):
                if i & (1<<j):
                    mini_sub.append(nums[j])
            result.append(mini_sub)
        return result
'''
To solve it using bit wise operators, we observe a pattern that the number of subsets is dependant on the size of the input array as:
N = 1, No. of subsets = 2
N = 2, No. of subsets = 4
N = 3, No. of subsets = 8 and so on…
No. of subsets of input array of size N = 2N = [1 << n]

inside for loop we are checking particular bit to check whether to include number at this particular bit
'''
        