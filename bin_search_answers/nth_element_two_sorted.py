#strivers binary search on answers

'''
Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.


Example 1

Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5

Output: 6

Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

Example 2

Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7

Output: 256

Explanation: Final sorted array is - [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 7th element of this array is 256.

'''

'''
First, ensure that arr1 is the smaller array. If not, swap the arrays. Our goal is to treat arr1[] as the smaller array.
Calculate the length of the left half as left = k.
Initialize two pointers:
low will point to max(0, k - n2),
high will point to min(k, n1) (n1 is the size of the smaller array and n2 is the size of the larger array).
Calculate 'mid1' and 'mid2':
mid1 = (low + high) // 2 (integer division),
mid2 = left - mid1.
Inside the loop, calculate l1, l2, r1, and r2:
l1 = arr1[mid1 - 1],
l2 = arr2[mid2 - 1],
r1 = arr1[mid1],
r2 = arr2[mid2].
If mid1 or mid2 is out of bounds, set l1, l2 to INT_MIN and r1, r2 to INT_MAX.
Eliminate halves based on the following conditions:
If l1 <= r2 and l2 <= r1, the answer is found. Return the maximum of l1 and l2.
If l1 > r2, eliminate the right half by setting high = mid1 - 1.
If l2 > r1, eliminate the left half by setting low = mid1 + 1.
When the loop terminates, include a dummy return statement to avoid warnings or errors.
'''

'''
low = max(0,k-m) because we must need atleast that much element to keep correct solution

high = min(k,n) because if we set high=n what if k<n then we encounter incorrect solution because we included more elements then needed
'''

class Solution:
    def kthElement(self, a, b, k):
        if len(a)>len(b):
            a,b = b,a
        n,m = len(a),len(b)
        low,high = max(0,k-m),min(k,n)
        while(low<=high):
            midA = (low+high)//2
            midB = k-midA
            leftA = float('-inf') if midA==0 else a[midA-1]
            rightA = float('inf') if midA==n else a[midA]
            leftB = float('-inf') if midB==0 else b[midB-1]
            rightB = float('inf') if midB==m else b[midB]

            if leftA<=rightB and leftB<=rightA:
                return max(leftA,leftB)
            if leftA>rightB:
                high = midA-1
            else:
                low = midA+1
        return 0

        # count=0
        # i,j=0,0
        # while i<len(a) or j<len(b):
        #     if a[i] and b[j]:
        #         if a[i]<b[j]:
        #             count+=1
        #             if count==k:
        #                 return a[i]
        #             i+=1
        #         else:
        #             count+=1
        #             if count==k:
        #                 return b[j]
        #             j+=1
        #     else:
        #         if a[i]:
        #             count+=1
        #             if count==k:
        #                 return a[i]
        #             i+=1
        #         else:
        #             count+=1
        #             if count==k:
        #                 return b[j]
        #             j+=1
        # return 0

