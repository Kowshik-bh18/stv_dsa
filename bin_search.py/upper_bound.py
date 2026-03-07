'''
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.

The upper bound of x is defined as the smallest index i such that nums[i] > x.

If no such index is found, return the size of the array.

'''


class Solution:
    def upperBound(self, nums, x):
        left=0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]<=x:
                left=mid+1
            else:
                right = mid-1
        return left
        