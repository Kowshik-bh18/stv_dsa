
'''
We cannot apply binary search on the answer space here as we cannot assure which missing number has the possibility of being the kth missing number. That is why, we will do something different here. We will try to find the closest neighbors (i.e. Present in the array) for the kth missing number by counting the number of missing numbers for each element in the given array.

Algorithm
Start by setting two markers: one at the beginning and one at the end of the list.
Keep checking the middle position between the two markers by taking their average.
Count how many numbers are missing up to that middle position by subtracting the expected number from the actual number found at that point.
If the number of missing values is less than the desired position, move your focus to the right side of the list by shifting the beginning marker ahead.
If not, move your focus to the left side by shifting the end marker backward.
Once you've narrowed down the search and exited the loop, return the final answer by adding the desired position to the last marker you checked (plus one).


ans = arr[high] + (k - missing[high])

missing[high] = (missing[high]-(high+1))

'''
from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # for i in range(1,max(arr)+k+1):
        #     if i not in arr:
        #         k-=1
        #     if k==0:
        #         return i

            #clever solution

            # for i in arr:
            #     if i<=k:
            #         k+=1
            #     if i>k:
            #         break
            # return k

            #bin_search

            left=0
            right = len(arr)-1
            while(left<=right):
                mid = (left+right)//2
                miss_n_b = arr[mid]-(mid+1)
                if miss_n_b<k:
                    left = mid+1
                else:
                    right = mid-1
            return right+k+1
        