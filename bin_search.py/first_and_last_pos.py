from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_left(nums,target),self.find_right(nums,target)]


    def find_left(self,nums,target):
        left=0
        right=len(nums)-1
        index=-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
            if nums[mid]==target:
                index=mid
        return index

    def find_right(self,nums,target):
        left=0
        right=len(nums)-1
        index=-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
            if nums[mid]==target:
                index=mid
        return index

'''
here we need two extra variables to keep track of first and last index of target
occurances

''' 

'''
The below problem is similar to above problem only due to sorted nature of array

Count Occurrences in a Sorted Array
Subscribe to TUF+

Hints
Company
You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.



Return the count of occurrences of target in the array.


Example 1

Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1

Output: 3

Explanation: The number 1 appears 3 times in the array.

Example 2

Input: arr = [5, 5, 5, 5, 5, 5], target = 5

Output: 6

Explanation: All elements in the array are 5, so the target appears 6 times.

'''