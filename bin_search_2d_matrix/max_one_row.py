'''
Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.

If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.


Example 1

Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]

Output: 0

Explanation: The row with the maximum number of ones is 0 (0 - indexed).

Example 2

Input: mat = [ [0, 0], [0, 0] ]

Output: -1

Explanation: The matrix does not contain any 1. So, -1 is the answer.
'''

class Solution:

    # 🔴 1. Brute Force (O(n * m))
    def rowWithMax1s_bruteforce(self, mat):
        n = len(mat)
        m = len(mat[0])

        maxi = 0
        indx = -1

        for i in range(n):
            count = sum(mat[i])   # count 1s in row
            if count > maxi:
                maxi = count
                indx = i

        return indx


    # 🟡 2. Binary Search (O(n log m))
    def rowWithMax1s_binary(self, mat):

        def last_zero(arr):
            low, high = 0, len(arr) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == 0:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        n = len(mat)
        m = len(mat[0])

        maxi = 0
        indx = -1

        for i in range(n):
            pos = last_zero(mat[i])

            if pos == -1:
                ones = m
            else:
                ones = m - (pos + 1)

            if ones > maxi:
                maxi = ones
                indx = i

        return indx


    # 🟢 3. Optimal (O(n + m))
    def rowWithMax1s_optimal(self, mat):
        n = len(mat)
        m = len(mat[0])

        i = 0
        j = m - 1
        indx = -1

        while i < n and j >= 0:
            if mat[i][j] == 1:
                indx = i
                j -= 1   # move left
            else:
                i += 1   # move down

        return indx