class Solution:
    def getFloorAndCeil(self, nums, x):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == x:
                return nums[mid], nums[mid]
            elif nums[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        floor = nums[right] if right >= 0 else -1
        ceil = nums[left] if left < len(nums) else -1

        return floor, ceil
    
'''
After binary search ends:

right = floor index
left  = ceil index

last two lines floor and ceil is to handle the the edge case when target is outside 

the array range 


for example if array is [2,3,4,5]

if target is 1

then without those conditions this will fail 

so those conditions are necessary for proper edge case handling
'''