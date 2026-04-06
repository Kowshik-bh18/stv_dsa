from typing import List
'''
1️⃣ Property of the Sorted Array

In this problem:

The array is sorted

Every element appears exactly twice

Only one element appears once

Example:

[1,1,2,2,3,3,4,5,5,6,6]
             ↑
        single element
2️⃣ Pattern Before and After the Single Element

Before the single element, pairs follow this pattern:

Index: 0 1 2 3 4 5
Value: 1 1 2 2 3 3
        ↑ ↑
      even odd

So before the single element:

nums[even] == nums[even+1]

Example:

nums[0] == nums[1]
nums[2] == nums[3]
nums[4] == nums[5]

After the single element appears, the pattern shifts.

Example:

[1,1,2,2,3,3,4,5,5,6,6]
             ↑

Indexes after shift:

Index: 6 7 8 9 10
Value: 4 5 5 6 6
        ↑ ↑
      odd even

Now pairs follow:

nums[odd] == nums[odd+1]
3️⃣ Why Your Condition Works

Your condition:

elif (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
    left = mid+1

This means:

The pair pattern is still correct

So the single element must be on the right

Example:

[1,1,2,2,3,3,4,5,5]
 mid

If mid is part of a correct pair, the single element has not appeared yet → go right.

4️⃣ When Pattern Breaks

Else:

right = mid - 1

Meaning:

The pair alignment is broken

That only happens after the single element

So the answer is on the left

5️⃣ Visual Example

Array:

[1,1,2,2,3,3,4,5,5]
           ↑

If mid = 2

nums[2] = 2
nums[3] = 2

Pair correct → single element is right side

If mid = 7

nums[7] = 5
nums[6] = 4

Pair broken → single element is left side

6️⃣ Time Complexity

Binary search → O(log n)

'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        left = 1
        right = n-2
        while(left<=right):
            mid =(left+right)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                left = mid+1
            else:
                right = mid-1

        


