'''Think of the rotated sorted array as two sorted halves the rotation “break” point is where the smallest element lives. Using binary search, we can efficiently zoom in on this smallest element by comparing middle elements to the rightmost element. If the middle element is greater than the rightmost element, the rotation point is to the right. Otherwise, it's to the left or could be the middle itself. This way, we reduce the search space by half each time, getting the rotation count in O(log n).

Imagine searching for the break in a long sorted belt by cutting it in halves repeatedly instead of scanning all the way through.
Initialize low = 0 and high = n - 1.
While low is less than high:
Find mid index.
If the element at mid is greater than the element at high, the rotation point is after mid, so update low = mid + 1.
Else, the rotation point is at mid or before it, so update high = mid.
When low meets high, that index is the rotation count (index of smallest element).'''

class Solution:
    # Function to find rotation count using binary search
    def findRotations(self, arr):
        low = 0
        high = len(arr) - 1

        # Loop until low meets high
        while low < high:
            mid = low + (high - low) // 2

            # If mid element is greater than element at high,
            # smallest element lies to the right of mid
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                # Else smallest element is at mid or to the left
                high = mid

        # When low == high, we found the smallest element
        return low

# Driver code
if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2,3]
    sol = Solution()
    rotations = sol.findRotations(arr)
    print(rotations)
