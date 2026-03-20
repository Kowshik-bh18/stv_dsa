'''
To find the N-th root of a number M, instead of checking every number from 1 to M (which is inefficient), we use binary search to efficiently reduce the search space. Since the N-th root lies between 1 and M, we start with a search range from 1 to M. For each middle value in this range, we compute its N-th power by multiplying it with itself N times, without using built-in power functions (to avoid integer overflow). During this multiplication, if the result exceeds M, we stop early to save time. If the final result equals M, we’ve found the N-th root. Otherwise, we adjust our search range accordingly to continue the binary search. This method significantly speeds up the process by halving the range at each step.
Start binary search with low as 1 and high as M.
Find mid of the range and multiply it with itself N times to get Nth power of mid.
If Nth power of mid equals M, return mid as the N-th root.
If Nth power of mid is less than M, shift search to the right half.
If Nth power of mid is greater than M, shift search to the left half.
If no integer root is found after the loop, return -1.
'''


# if they need answer without concerning about int or float
def nth_root(n, m):
    low = 1
    high = m
    eps = 1e-6   # precision

    while (high - low) > eps:
        mid = (low + high) / 2
        if mid ** n < m:
            low = mid
        else:
            high = mid

    return low

'''
Final Complexity
O(nlog(m/ϵ))
'''

#if they like below

'''Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.


Example 1

Input: N = 3, M = 27

Output: 3

Explanation: The cube root of 27 is equal to 3.

'''

class Solution:
    def NthRoot(self, n, m):
        low =1
        high = m
        while low<=high:
            mid = (low+high)//2
            val = mid**n
            if val==m:
                return mid
            elif val<m:
                low = mid+1
            else:
                high = mid-1
        return -1
    

'''
Time Complexity: O(logM), we search for every possible number from 1 to M to check if it is the Nth root.
Space Complexity: O(1), constant additional space is used.
'''

      
      

