'''
simple template mainly based the trick:- In rotated sorted array always one half 
 is sorted
'''

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[left]<=nums[mid]:
                if (target>=nums[left] and target<=nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                if (target>=nums[mid] and target<=nums[right]):
                    left = mid+1
                else:
                    right = mid-1
        return -1



'''
similar to above but above solution fails if array conatain duplicate especially in 
following case:
[1,0,1,1,1]

here

Example Where Normal Logic Fails

Array:

nums = [1,0,1,1,1]
target = 0

This is a rotated sorted array with duplicates.

Step 1
left = 0
right = 4
mid = 2

Values:

nums[left] = 1
nums[mid]  = 1
nums[right]= 1

Array view:

[1, 0, 1, 1, 1]
 L     M     R
Step 2 — Normal Logic

Your normal algorithm checks:

nums[left] <= nums[mid]
1 <= 1 → TRUE

So it assumes left half is sorted:

[1,0,1]

But actually:

1 → 0 → 1

This is NOT sorted ❌

The algorithm got confused because of duplicates.

Step 3 — Wrong Decision

It checks if target is inside:

nums[left] <= target <= nums[mid]

1 <= 0 <= 1 → FALSE

So it searches the right half:

left = mid + 1

Now:

[1,1]

But the target 0 was in the left side.

So the algorithm loses the correct region.

Why This Happens

Because when:

nums[left] == nums[mid] == nums[right]

You cannot determine which side is sorted.

Both halves look identical.

[1, ?, 1, ?, 1]

So the algorithm becomes ambiguous.

How the Correct Solution Fixes This

When we see:

nums[left] == nums[mid] == nums[right]

We simply shrink:

left += 1
right -= 1

This removes duplicates from edges.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:
                if target>=nums[left] and target<=nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False

         
