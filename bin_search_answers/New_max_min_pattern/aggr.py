'''
It is pattern under max(min)
we have place cow anywhere in stalls and we have to take minimum of that then at last we want maxium of all this minimum

Intuition
The basic idea is to test every possible distance between 1 and the difference between the farthest and nearest stalls. The largest distance for which canWePlace() returns true will be our answer.

Algorithm:
Sort the stalls array in increasing order.
Use a loop to check every possible distance one by one.
For each distance, call the canWePlace() function to see if all cows can be placed:
If canWePlace() returns false for a distance, return the previous distance (current distance - 1), as that was the largest distance where placement was possible.
If the loop finishes without failure, return the largest possible distance (difference between farthest and nearest stalls).



We use Binary Search to optimize the solution by reducing the answer space in half each time.

The main idea of Binary Search is to determine which half of the search space can be eliminated based on a specific condition, thus minimizing unnecessary checks.

The answer space is sorted: 1 to the difference between max and min values. We can divide this space into two parts:

One containing valid answers.
The other containing non-viable options.
Example: For stalls = {1, 2, 8, 4, 9}, the possible distances are shown below:

Sort the stalls: Arrange the stalls in ascending order.
Set the search range:
Start with the smallest possible distance.
The largest possible distance is the gap between the farthest and nearest stalls.
Use Binary Search: Repeat the process until the search range is exhausted:
Pick the middle distance: Test this distance as a possible answer.
Check if it works:
If it works: Try to increase the distance to see if a larger one is possible.
If it doesn’t work: Decrease the distance and test smaller ones.
Return answer: After exiting the loop, high holds the largest valid distance.
'''
class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()
        def can_place(dis):
            cow_placed = 1
            last_cow = nums[0]
            for i in range(1,len(nums)):
                if (nums[i]-last_cow)>=dis:
                    cow_placed+=1
                    last_cow = nums[i]
            return cow_placed>=k


        # brute force approach
        # for i in range(1,(max(nums)-min(nums))+1):
        #     if can_place(i):
        #         continue
        #     else:
        #         return i-1
        # return (max(nums)-min(nums))



        #binary search approach
        left = 1
        right = max(nums)-min(nums)
        while(left<=right):
            mid = (left+right)//2
            if can_place(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans


        