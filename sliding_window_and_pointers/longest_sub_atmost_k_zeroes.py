from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        n_zer=0
        max_len =0
        for right in range(len(nums)):
            if nums[right]==0:
                n_zer+=1
            if n_zer>k:
                if nums[left]==0:
                    n_zer-=1
                left+=1
            if n_zer<=k:
                max_len = max(max_len,right-left+1)
        return max_len


'''
🔎 Time & Space Complexity

Time Complexity: O(n)
Each element is visited at most twice (once by right, once by left).

Space Complexity: O(1)
Only a few variables are used.

You cannot do better than O(n) because you must inspect every element at least once.
'''

'''
🔥 Slightly Cleaner Version (Same Optimal Complexity)

we can simplify the logic a bit:

This below approach works because we make sure that maximum window will be maintained until we get another maximum window

But main thing is we never allow window to shrink behind maximum
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left + 1
    

# logical intuition
'''
We can optimize the standard sliding window approach by eliminating the inner while-loop. Instead of using an explicit loop to shrink the window when the number of zeros exceeds the allowed flips (K), we can use a single conditional check to move the left pointer forward only when needed. This ensures that each pointer moves in a controlled and efficient manner without unnecessary loop nesting. The logic remains similar to the standard sliding window, but this structure can make the code slightly faster and cleaner in certain languages.
Initialize two pointers, left and right, both set to 0, and a variable zerocount to keep track of the number of zeros in the current window.
Traverse the array using the right pointer.
If the current element is 0, increment zerocount.
If zerocount exceeds k, check if the element at the left pointer is 0, and if so, decrement zerocount. Then increment the left pointer.
At each step, calculate the current window size and update the maximum length if it's greater than the previously recorded maximum.
Continue this process until the right pointer has traversed the entire array.
Return the maximum window size found.
'''
