from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1 
        ans = float('inf')
        while(left<=right):
            mid = (left+right)//2
            if nums[left]<=nums[mid]:
                ans = min(ans,nums[left])
                left = mid+1
            else:
                ans = min(ans,nums[mid])
                right = mid-1
        return ans
    

#further optimized solution

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ans = float('inf')
        while(left<=right):
            mid = (left+right)//2
            if nums[left]<=nums[right]:
                ans = min(ans,nums[left])
                break
            elif nums[left]<=nums[mid]:
                ans = min(ans,nums[left])
                left = mid+1
            else:
                ans = min(ans,nums[mid])
                right = mid-1
        return ans
        
        

    class Solution:
    # Function to find the minimum element using binary search
        def findMin(self, nums):

        # Initialize low and high pointers
            low, high = 0, len(nums) - 1

        # Binary search loop
            while low < high:

            # Calculate mid index
                mid = low + (high - low) // 2

            # Check which half to discard
                if nums[mid] > nums[high]:

                # Minimum lies in right half
                    low = mid + 1

                else:

                # Minimum lies in left half (including mid)
                    high = mid

        # Return the minimum element
            return nums[low]

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)


'''
1️⃣ The Key Reason

Because mid itself could be the minimum element.

So we cannot discard it.

2️⃣ Example Where mid IS the Minimum

Array:

[6,7,0,1,2,3,4]

Suppose:

low = 0
high = 6
mid = 2

Array view:

6 7 0 1 2 3 4
    ^
   mid

Values:

nums[mid] = 0
nums[high] = 4

Check condition:

nums[mid] > nums[high]
0 > 4  ❌

So we go to else:

high = mid

Now:

low = 0
high = 2

We keep index 2, which is the minimum.

3️⃣ What If We Did high = mid - 1 ?

If we did:

high = mid - 1

Then:

high = 1

Array becomes:

[6,7]

But we removed the minimum (0).

The algorithm would fail.

4️⃣ So the Rule Is

When:

nums[mid] <= nums[high]

we know:

minimum is in left side INCLUDING mid

So we write:

high = mid

Not mid-1.

5️⃣ But When We Move Left Pointer

We write:

low = mid + 1

because when:

nums[mid] > nums[high]

we know:

mid CANNOT be minimum

Example:

4 5 6 7 | 0 1 2
      ^
     mid

Minimum must be after mid, so we safely discard it.

6️⃣ Summary Rule
Condition	Move
nums[mid] > nums[high]	low = mid + 1
nums[mid] <= nums[high]	high = mid
7️⃣ One Simple Memory Trick

Think like this:

mid might be minimum → keep it
mid cannot be minimum → discard it

So:

keep mid → high = mid
discard mid → low = mid + 1

'''