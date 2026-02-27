class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        

'''
Approach
Two-Pointer (In-Place Swapping)

Key Points:
j is used to track the position to place the next non-zero element.

The loop goes through each element i:

If nums[i] is non-zero, it swaps nums[i] with nums[j], and increments j.

Example:
Input: [0, 1, 0, 3, 12]

Step-by-step after each iteration:

i=0: nums[0] = 0 → skip

i=1: nums[1] = 1 → swap with nums[0] → [1, 0, 0, 3, 12]

i=2: nums[2] = 0 → skip

i=3: nums[3] = 3 → swap with nums[1] → [1, 3, 0, 0, 12]

i=4: nums[4] = 12 → swap with nums[2] → [1, 3, 12, 0, 0]

Final output: [1, 3, 12, 0, 0]

Complexity
Time complexity: O(n)
Each element is visited exactly once in the for loop (i goes from 0 to n - 1).
Space Complexity: O(1)
The algorithm uses only a constant amount of extra space (int j, or just variables for indexing/swapping).
It modifies the array in-place, without using extra arrays or lists.
'''
