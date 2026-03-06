#This is the pattern which will work if condition is not monotonic and counting the subarray problems

class Solution:
    # Function to compute number of subarrays with sum exactly equal to goal
    def numSubarraysWithSum(self, nums, goal):
        # Return difference between atMost(goal) and atMost(goal - 1)
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)

    # Helper function to compute subarrays with sum at most k
    def atMost(self, nums, k):
        # No subarrays for negative sum
        if k < 0:
            return 0

        left = 0
        total = 0
        curr_sum = 0

        # Traverse array using right pointer
        for right in range(len(nums)):
            # Add current element to sum
            curr_sum += nums[right]

            # Shrink window if sum exceeds k
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            # Add number of valid subarrays ending at right
            total += (right - left + 1)

        return total

# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(sol.numSubarraysWithSum(nums, goal))  # Output: 4


'''
To count the number of subarrays with sum exactly equal to goal, a clever strategy is to reframe the problem: We count the number of subarrays whose sum is at most goal, and subtract from it the number of subarrays whose sum is at most goal- 1.

This works because:The subarrays with sum exactly goal are the ones included in atMost(goal) but not in atMost(goal - 1) and This is valid for non-negative elements.

Why is this more efficient?
Instead of recomputing subarray sums from scratch , we maintain a sliding window that expands and contracts based on the current sum.This gives us linear time performance by moving each pointer at most once. This method only works when goal ≥ 1, because the atMost(goal - 1) calculation is invalid for goal = 0 (negative index/window not possible).
Define a helper function to calculate the number of subarrays with sum at most a given value
Initialize a sliding window with two pointers (left and right)
Iterate through the array, expanding the right pointer and adding to current sum
If the current sum exceeds the target, shrink the window from the left until it’s valid
At each step, add the size of the current valid window to the count
To get the final answer, compute: atMost(goal) - atMost(goal - 1)


'''


#similar problem

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.sub(nums,k)-self.sub(nums,k-1)


    def sub(self,s,tar):
        left=0
        hash_map = {}
        count=0
        for right in range(len(s)):
            hash_map[s[right]]= hash_map.get(s[right],0)+1
            while len(hash_map)>tar:
                hash_map[s[left]]-=1
                if hash_map[s[left]]==0:
                    del hash_map[s[left]]
                left+=1
            count+=(right-left+1)
        return count


        