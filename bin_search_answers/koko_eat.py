'''
The naive method checks every speed, which is slow if the piles are large. But the possible answer space (from 1 to the maximum pile size) is sorted, meaning if a certain speed works, then all higher speeds will also work. This allows us to apply Binary Search on the answer space to efficiently find the minimum speed at which Koko can finish the bananas within the given hours.
First, identify the largest pile size since the eating speed cannot be more than that.
Set the search range with the lowest speed as 1 and the highest speed as the maximum pile size.
Use binary search within this range to check possible speeds.
At each step, take the middle value as the current speed and calculate how many hours it would take to finish all piles at this speed.
If the total hours are less than or equal to the allowed hours, this speed is a candidate, so try to see if a smaller speed also works by moving left.
If the total hours exceed the allowed hours, then the speed is too slow, so move right to try higher speeds.
Continue this process until the range closes, and the smallest valid speed found will be the answer.

'''

import math
class Solution:
    def minimumRateToEatBananas(self, nums, h):
        left = 1
        right = max(nums)
        ans = right  # initialize answer as max speed
        
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for ban in nums:
                time += math.ceil(ban / mid)
            
            if time <= h:
                ans = mid      # mid works, try smaller
                right = mid - 1
            else:
                left = mid + 1  # mid too slow, try bigger
        
        return ans