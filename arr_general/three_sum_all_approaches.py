#🔥 3Sum – All Approaches

'''Problem:
Given an array nums, return all unique triplets [a,b,c] such that:

a + b + c = 0
🥉 Approach 1: Brute Force (Triple Loop)
Idea

Try every triplet.
'''
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = set()
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return list(result)
'''
⏱ Complexity

Time: O(n³)

Space: O(n)

❌ Very slow
Only for understanding.
'''



# 🥈 Approach 2: Better – Hashing (Two Sum Inside Loop)


# Fix one number, then solve Two Sum = -nums[i] wkt a+b+c = target then c = target-b-a

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = set()
        
        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)
                seen.add(nums[j])
        
        return list(result)
'''
⏱ Complexity

Time: O(n²)

Space: O(n)

Better than brute force.

But:

Needs sorting triplets

Needs set to remove duplicates
'''

# 🥇 Approach 3: Optimal – Sorting + Two Pointers

'''🔥 This is the standard interview solution.

Idea

Sort the array

Fix one element

Use two pointers for remaining two numbers
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n):
            
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result
    
'''
⏱ Complexity

Sorting: O(n log n)

Two pointers loop: O(n²)

Overall:

Time: O(n²)
Space: O(1) (ignoring output)

This is the best possible for 3Sum.

You cannot do better than O(n²).

🧠 Why Sorting Is Powerful

After sorting:

If sum too small → move left++

If sum too big → move right--

That reduces one loop.

Without sorting, you cannot use two pointers.

🎯 Important Edge Cases

Skip duplicate i

Skip duplicate left

Skip duplicate right

Otherwise duplicates appear.

🧠 Deep Pattern Insight

3Sum =

Fix one element
Solve 2Sum on remaining

4Sum =

Fix one
Solve 3Sum

kSum generalizes this.

🚀 Interview Tip

If interviewer asks:

“Can you do better than O(n²)?”

Answer:

❌ No — because we must examine pairs.

That shows understanding of lower bound.
'''