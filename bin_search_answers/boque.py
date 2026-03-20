'''
If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and we will return -1.
Next, we will find the maximum element i.e. max(arr[]), and the minimum element i.e. min(arr[]) in the array.
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to min(arr[]) and the high will point to max(arr[]).
Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division)
Eliminate the halves based on the value returned by possible(): We will pass the potential answer, represented by the variable 'mid' (which corresponds to a specific day), to the 'possible()' function.
If possible() returns true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

'''

'''
Time Complexity: O(1) O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.

Space Complexity : O(h)O(1) as we are not using any extra space to solve this problem.
'''
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_possible(i):
            track = 0
            boq = 0
            for flow in bloomDay:
                if flow<=i:
                    track+=1
                else:
                    track = 0
                if track==k:
                    boq+=1
                    track = 0
            if boq>=m:
                return i
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        ans  = -1
        while(left<=right):
            mid = (left+right)//2

            if is_possible(mid)!=-1:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans