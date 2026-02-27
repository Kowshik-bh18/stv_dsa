'''Let’s see Two Sum – All 3 Approaches clearly.

Problem:

Given an array and a target, return indices of two numbers such that they add up to target.

Example:

nums = [2,7,11,15]
target = 9
Output = [0,1]
✅ 1️⃣ Brute Force Approach
💡 Idea:

Check every pair.
'''
 # Code:
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
            
'''
⏱ Time Complexity:

O(n²)

🗂 Space Complexity:

O(1)

✔ When to use?

Only for understanding. Not efficient for interviews.

'''

'''
✅ 2️⃣ Better Approach (Sorting + Two Pointers)
💡 Idea:

Sort array

Use two pointers (left, right)

⚠️ Problem: Sorting changes indices, so you must store original index.
'''

# Code:
def twoSum(nums, target):
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort()

    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left][0] + arr[right][0]
        if total == target:
            return [arr[left][1], arr[right][1]]
        elif total < target:
            left += 1
        else:
            right -= 1

'''
⏱ Time Complexity:

O(n log n) (because of sorting)

🗂 Space Complexity:

O(n)

✔ When to use?

Useful when:

Array is already sorted

Or you don’t care about original indices

✅ 3️⃣ Optimal Approach (HashMap)

🔥 Most asked in interviews

💡 Idea:

Store number and its index in hashmap.

For each number:

Check if target - num exists

If yes → return indices
'''
# Code:
def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[nums[i]] = i
'''
⏱ Time Complexity:

O(n)

🗂 Space Complexity:

O(n)

🧠 Interview Explanation in 3 Lines

Brute force → check all pairs → O(n²)

Sorting + two pointers → O(n log n)

HashMap → store visited elements → O(n) optimal

Since you’re preparing seriously for placements now, remember:

👉 If interviewer says “optimize it” → immediately say HashMap approach.
'''