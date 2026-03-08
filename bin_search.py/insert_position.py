from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return left
'''
solution is exactly similar to lower bound because if target element is not found 
left will be in correct insert position automatically

Time complexity:- o(logn)->because each time we halve the search space 
space complexity:-o(1)
'''