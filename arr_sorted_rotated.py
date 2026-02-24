#problem statement
'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

'''

# solution

l = [5,1,2,3,4]
class Solution:
    def check(self, nums: List[int]) -> bool:
        is_s = 0
        for i in range(len(nums)-1):
            if(nums[i+1]<nums[i]):
                is_s+=1
        if(nums[0]<nums[-1]):
            is_s+=1
        if is_s<=1:
            return True
        return False


class Solution:     #another good approach to exit earlier and we can naturally simulate wrap up using modulo operator
    def check(self, nums: List[int]) -> bool:
        flag = False

        for i in range(len(nums)):
            if nums[(i+1) % len(nums)] < nums[i]:
                if flag:
                    return False
                flag = True
        return True
    

#logical intuition

'''
Intuition
The problem requires checking if a given array is sorted or can be rotated to become sorted. A sorted and rotated array has at most one "drop" (where a number is greater than the next number). If there is more than one such drop, the array cannot be a valid rotation of a sorted array.

Approach
Initialize a flag variable as false to track if a drop in order has been found.
Iterate through the array, comparing each element nums[i] with the next element nums[(i + 1) % nums.size()] (using modulo to handle wrap-around).
If a drop (nums[i] > nums[(i + 1) % nums.size()]) is found:
i. If flag is already true, return false because more than one drop means it is not a rotated sorted array.
ii. Otherwise, set flag = true to mark the first drop.
If the loop completes with at most one drop, return true.
Complexity
Time complexity:
O(n)

Space complexity:
O(1)
'''