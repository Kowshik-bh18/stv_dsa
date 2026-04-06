'''
In addition to the two cases above, we can have two more cases. One, where the current element itself is the peak or where the current element is a common point where a decreasing sequence ends and an increasing sequence begins. In either cases we can eliminate any of the halves, as the other half will also contain a peak element.
Initialize the search space to the full range of the array.
Find the middle index of the current search range.
Check if the middle element is greater than its right neighbor.
If yes, then a peak must exist in the left half (including mid), so shrink the right bound.
Otherwise, the peak must lie in the right half (excluding mid), so shift the left bound.
Continue until the search space converges to a single element.
This final position is the index of a peak element.
'''

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        left=1
        right = n-2
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]>nums[left] and nums[mid]>nums[right]):
                return mid
            elif nums[mid]>nums[mid-1]:
                left = mid+1
            else:
                right = mid-1
        return -1


#another easy approach
'''
1️⃣ What the Algorithm Actually Guarantees

During the binary search for Find Peak Element, we maintain an invariant:

There is always at least one peak inside the range [left, right]


Every step removes only the side that cannot contain a peak.

2️⃣ How the Range Shrinks

We check:

nums[mid] < nums[mid+1]

Case 1 — Increasing slope
1 2 3 4 5 3 2
      mid


Since it is increasing, the peak must be to the right.

So we shrink:

left = mid + 1


Now range becomes:

[mid+1 ... right]


Peak still exists there.

Case 2 — Decreasing slope
1 4 6 5 3
      mid


Now we are descending.

So mid or something left of it is a peak.

We shrink:

right = mid


Range becomes:

[left ... mid]


Peak still exists.

3️⃣ Eventually the Range Becomes One Element

The search keeps shrinking:

[1 3 5 4 2]
 → [5 4 2]
 → [5]


Now:

left == right


At this moment:

only one index remains


But we maintained the rule:

a peak always exists in this range


So that remaining index must be the peak.

4️⃣ Why Returning left Works

When loop ends:

left == right


So both are the same index:

return left


or

return right


Both are correct.

5️⃣ Short Mental Model (Best Way to Remember)

Think of the algorithm as:

Follow the slope until you reach the top


If slope goes up → go right
If slope goes down → go left

Eventually you reach a top point (peak).

✅ Your statement rewritten correctly

The binary search keeps shrinking the range toward a region that must contain a peak. When the range reduces to one index (left == right), that index must be the peak.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left