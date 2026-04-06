'''
mplement Lower Bound


23

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

What is lower bound?
The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

'''

class Solution:
    def lowerBound(self, nums, x):
        left=0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==x:
                return mid
            elif nums[mid]<x:
                left = mid+1
            else:
                right = mid-1
        return left

       


