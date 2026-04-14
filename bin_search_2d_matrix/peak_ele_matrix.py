'''Find Peak Element - II

Hints
Company
Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j].A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.



Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.



Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.


Example 1

Input: mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]

Output: [1, 1]

Explanation: The value at index [1, 1] is 30, which is a peak element because all its neighbours are smaller or equal to it. Similarly, {2, 2} can also be picked as a peak.

Example 2

Input: mat=[[10, 7], [11, 17]]

Output : [1, 1]

Explanation:The value at index [1, 1] is 17, which is the only peak element because all its neighbours are smaller or equal to it.
'''

#brute force
'''
if we think bit one answer is obviously the maximum element in matrix
'''
class Solution:
    def findPeakGrid(self, mat):
        def get_element(matrix, i, j, default=-1):
            try:
                return matrix[i][j]
            except IndexError:
                return default

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                left=get_element(mat,i,j-1)
                right=get_element(mat,i,j+1)
                top = get_element(mat,i-1,j)
                down = get_element(mat,i+1,j)
                ele = get_element(mat,i,j)

                if ele>left and ele>right and ele>top and ele>down:
                    return [i,j]
        return [-1,-1]

#optimized approach
'''
almost similar to 1d array peak element

To solve this problem we use the binary search approach.
The key idea comes from how we find a peak in a 1-D array:
For any middle position (mid), we check if it’s larger than both its neighbors, if it is, we’ve found a peak.
If mid is smaller than the element on its left, that means a peak must be somewhere to the left, so we can discard the right half.
If mid is smaller than the element on its right, then a peak must lie to the right, allowing us to discard the left half.
This method reduces the number of elements we need to consider in every step, improving efficiency.
For a 2-D array,
The search will cover the column range from 0 to col-1, where col is the total number of columns.
We choose a middle column and identify the row with the largest element in that column.
We apply similar logic as in 1-D: if this element is bigger than both its side neighbors, we’ve found the peak.
If the left neighbor is bigger, we only search the left part; if the right neighbor is bigger, we search the right part.

'''
from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def find_max_ele(mat, row, col):
            index = -1
            maxi = float('-inf')
            for i in range(row):
                if mat[i][col] > maxi:
                    maxi = mat[i][col]
                    index = i
            return index
        
        row, col = len(mat), len(mat[0])
        left, right = 0, col - 1

        while left <= right:
            mid = (left + right) // 2
            maxi_indx = find_max_ele(mat, row, mid)

            left_val = mat[maxi_indx][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[maxi_indx][mid + 1] if mid + 1 < col else -1
            curr = mat[maxi_indx][mid]

            if curr > left_val and curr > right_val:
                return [maxi_indx, mid]
            elif left_val > curr:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]