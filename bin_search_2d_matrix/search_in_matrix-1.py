from typing import List

'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

'''


'''
it only works when each row is sorted and first element of each row is greater than last element of previous row

Because of this property we can treat this as 1D array and we can virtual map 1D array to 2D array using following formula

row = mid/(no of column) ->it gives row number since each start of row is multiple of no of column
col = md%(no of column)  ->it gives column numer inside the row 
'''


'''
If we flatten the given 2D matrix into a 1D array, that 1D array would also be sorted. By running binary search on this flattened version, we could quickly check if the element exists.

But actually flattening the matrix takes extra time and memory, which makes it inefficient. Instead, we can simulate the flattening without creating a new array. The trick is to directly map a 1D index into the corresponding row and column of the 2D matrix.

To do this mapping, if there are `m` columns in the matrix and the index is `i`, then:
Row = i / m, Column = i % m.

So instead of working on the 2D matrix directly, we pretend it’s a sorted 1D array of length (rows × columns), and apply binary search on this imaginary array.

Start with two pointers: one at the first index of the imaginary 1D array, and the other at the last index.
While the first pointer does not cross the last:
Find the middle index between the two pointers.
Convert this middle index into a row and column of the original 2D matrix.
If the element at that position matches the target, return true (element found).
If the element is smaller than the target, discard the left half and continue searching in the right half.
If the element is larger than the target, discard the right half and continue searching in the left half.
If the search ends without finding the element, return false (element not present in the matrix).

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        left,right=0,(n*m)-1
        while(left<=right):
            mid = (left+right)//2
            row = mid//m
            col = mid%m
            if(matrix[row][col]==target):
                return True
            elif matrix[row][col]<target:
                left = mid+1
            else:
                right = mid-1
        return False

        