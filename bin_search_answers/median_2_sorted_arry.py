'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        low, high = 0, n

        while low <= high:
            midA = (low + high) // 2
            midB = (n + m + 1) // 2 - midA

            leftA = float('-inf') if midA == 0 else nums1[midA - 1]
            rightA = float('inf') if midA == n else nums1[midA]

            leftB = float('-inf') if midB == 0 else nums2[midB - 1]
            rightB = float('inf') if midB == m else nums2[midB]

            if leftA <= rightB and leftB <= rightA:
                if (n + m) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return max(leftA, leftB)

            elif leftA > rightB:
                high = midA - 1
            else:
                low = midA + 1

        return 0