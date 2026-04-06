from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1

'''
Intuition
Since the array is sorted in ascending order, we can use Binary Search instead of checking every element.

Binary search works by repeatedly dividing the search space in half.

At each step:

Find the middle element

Compare it with the target

Decide whether to search left half or right half

Example:

nums = [1,3,5,7,9]
target = 7
left = 0
right = 4
mid = 2
nums[mid] = 5
Since:

7 > 5
We ignore the left half and search the right half.

Approach
Initialize two pointers:
left = 0

right = nums.length - 1
Continue searching while:
left <= right
Find the middle index:
mid = (left + right) / 2
Compare the target with the middle element:
If nums[mid] == target → return mid

If target > nums[mid] → search the right half

If target < nums[mid] → search the left half

If the target is not found after the loop ends, return -1.
'''
print(1//2)