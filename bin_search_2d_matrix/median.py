'''
Matrix Median
Subscribe to TUF+

Hints
Company
Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.


Example 1

Input: matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 

Output: 5

Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5

Example 2

Input: matrix=[ [1, 3, 8], [2, 3, 4], [1, 2, 5] ] 

Output: 3

Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 8. So, median = 3

'''


'''
In a row-wise sorted matrix, each row is individually sorted, but the entire matrix isn’t globally sorted. Hence, we can’t just pick the middle element directly to get the median. If we flatten and sort the entire matrix, it would take O(N×M log(N×M)) time, which is inefficient. Instead, we can take advantage of the sorted rows and apply a more optimized method using binary search on the value space (i.e., the range of possible numbers in the matrix).

We start by finding the minimum and maximum elements in the matrix. The smallest element will be in the first column, and the largest element will be in the last column. We then binary search between this range to find the median value.

In each iteration of the binary search, we choose a middle value and count how many elements in the matrix are less than or equal to it. Since each row is sorted, we can do this efficiently using binary search (upper bound) on each row. If the count is less than or equal to half of the total number of elements, we move our search range to the right, otherwise, we move it to the left.


'''

class Solution:
    def findMedian(self, matrix):
        row, col = len(matrix), len(matrix[0])

        def upper_bound(arr, low, high, ele):
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= ele:
                    low = mid + 1
                else:
                    high = mid - 1
            return low   # count of elements <= ele

        # search space
        low = min(r[0] for r in matrix)
        high = max(r[-1] for r in matrix)

        req = (row * col) // 2

        def count_less_equal(x):
            count = 0
            for arr in matrix:
                count += upper_bound(arr, 0, len(arr) - 1, x)
            return count

        while low <= high:
            mid = (low + high) // 2
            less_ele = count_less_equal(mid)

            if less_ele <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low
    


# simplified solution using bisect 

import bisect

class Solution:
    def findMedian(self, matrix):
        row, col = len(matrix), len(matrix[0])

        low = min(r[0] for r in matrix)
        high = max(r[-1] for r in matrix)

        req = (row * col) // 2

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for arr in matrix:
                count += bisect.bisect_right(arr, mid)

            if count <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low