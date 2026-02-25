'''
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Example 1

Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2

Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation:

The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
'''

i = j = 0
result = []

while i < len(nums1) and j < len(nums2):

    if i > 0 and nums1[i] == nums1[i - 1]:
        i += 1
        continue

    if j > 0 and nums2[j] == nums2[j - 1]:
        j += 1
        continue

    if nums1[i] < nums2[j]:
        result.append(nums1[i])
        i += 1
    elif nums1[i] > nums2[j]:
        result.append(nums2[j])   # ✅ fixed
        j += 1
    else:
        result.append(nums1[i])
        i += 1
        j += 1


while i < len(nums1):
    if i == 0 or nums1[i] != nums1[i - 1]:
        result.append(nums1[i])
    i += 1

while j < len(nums2):
    if j == 0 or nums2[j] != nums2[j - 1]:
        result.append(nums2[j])
    j += 1
    
#intuition
'''
Since both arrays are sorted, we can efficiently find their union by iterating through them simultaneously. Using two pointers, one for each array, we compare elements and add the smaller one to the result (skipping duplicates). If elements are equal, add once and move both pointers. This way, we merge the arrays like in merge sort, avoiding extra space for maps or sets and achieving linear time complexity.
Initialize two pointers at the start of both arrays.
While neither pointer has reached the end:
If element pointed by first pointer is smaller, add it to result if not duplicate, move first pointer.
If element pointed by second pointer is smaller, add it to result if not duplicate, move second pointer.
If both elements are equal, add one to result if not duplicate, move both pointers.
After exiting loop, append remaining elements from either array, skipping duplicates.
Return the result array containing the union.
'''