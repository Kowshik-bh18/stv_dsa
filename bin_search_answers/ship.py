'''
We want to find the minimum ship capacity that allows shipping all packages within the given number of days. The capacity must be at least the heaviest package because you can’t split a package. At the same time, the capacity can be at most the sum of all packages (if you ship everything in one day). So the answer lies between these two extremes. Using binary search on this range lets us efficiently find the smallest capacity that works. For each candidate capacity, we check if it’s possible to ship all packages within the given days by greedily accumulating package weights until we reach capacity, then moving to the next day.
Set the lower bound as the maximum weight in the packages.
Set the upper bound as the sum of all package weights.
While the lower bound is less than or equal to the upper bound, do:
Pick the middle value between lower and upper bounds as the candidate capacity.
Simulate shipping with this capacity: accumulate package weights until capacity is reached, then count a day and reset accumulation.
If the number of days used is within the allowed days, move the upper bound down to try smaller capacities.
If the number of days exceeds the allowed days, increase the lower bound to try larger capacities.
Return the lower bound when the search finishes as the minimum capacity needed.

'''

from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_ship(i):
            tot_sum = 0
            tot_days= 1
            for weight in weights:
                tot_sum+=weight
                if tot_sum>i:
                    tot_days+=1
                    tot_sum = weight
            return tot_days<=days
        left = max(weights)
        right = sum(weights)
        while(left<=right):
            mid = (left+right)//2
            if is_ship(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans

        