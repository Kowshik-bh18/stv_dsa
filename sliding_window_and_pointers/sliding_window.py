#r-1
# always remember left window pointer will always less than right window




'''

🔥 Sliding Window Technique (Complete Guide)
📌 What is Sliding Window?

Sliding Window is an optimization technique used on:

Arrays

Strings

Subarrays / Substrings

It helps reduce time complexity from O(n²) → O(n).

Instead of checking all subarrays, we maintain a window (range) and slide it intelligently.

🧠 When Should You Think of Sliding Window?

Ask yourself:

✅ Is it array/string?
✅ Is it asking about subarray / substring?
✅ Is it about contiguous elements?
✅ Is there a constraint like:

Sum

Length

Distinct characters

At most / exactly K

Longest / shortest

If YES → Sliding Window 💡

🪟 Types of Sliding Window

There are 2 main types:

Fixed Size Window

Variable Size Window

1️⃣ Fixed Size Sliding Window
📌 Used When:

Window size k is given

Example: "Maximum sum of subarray of size k"

🔍 Example 1:
Maximum Sum Subarray of Size K

Input:

arr = [2,1,5,1,3,2], k = 3
❌ Brute Force → O(n²)

Check all subarrays of size 3

✅ Sliding Window → O(n)
Logic:

Compute first window sum

Slide:

Remove left element

Add new right element

💻 Code:
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
⏱ Time: O(n)
📦 Space: O(1)
2️⃣ Variable Size Sliding Window

Used when:

Longest / smallest subarray

At most K distinct

Sum >= target

No repeating characters

Here window size is dynamic.

We use:

left = 0
for right in range(n):
    expand window
    
    while condition invalid:
        shrink window
        left += 1
🔍 Example 2:
Longest Substring Without Repeating Characters

Input:

s = "abcabcbb"

Output: 3 ("abc")

🧠 Logic:

Use a set

Expand right

If duplicate found → shrink from left

💻 Code:
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
⏱ Time: O(n)

Why O(n)?
Each element enters and leaves window once.

🔥 Most Important Pattern (Interview Pattern)
Template for Variable Window
left = 0

for right in range(len(arr)):
    # Expand
    add arr[right] to window
    
    # Shrink if invalid
    while condition_not_valid:
        remove arr[left]
        left += 1
    
    # Update answer
    ans = max(ans, right - left + 1)

This template solves 70% sliding window problems.

'''


def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    
    return max_count

# if they ask starting and ending of window

def findMaxConsecutiveOnesIndexes(nums):
    count = 0
    max_count = 0
    
    start = 0          # current streak start
    best_start = 0     # best streak start
    best_end = 0       # best streak end
    
    for i in range(len(nums)):
        if nums[i] == 1:
            if count == 0:
                start = i   # new streak starts
            
            count += 1
            
            if count > max_count:
                max_count = count
                best_start = start
                best_end = i
        else:
            count = 0
    
    return best_start, best_end