#same solution for both split and painter same min(max) pattern 

'''
observer this pattern carefully and it can be easily detected.


We are going to use the Binary Search algorithm to optimize the approach.

The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

Algorithm
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).
Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division.
Eliminate the halves based on the number of subarrays returned by countPartitions(): We will pass the potential value of ‘maxSum’, represented by the variable 'mid', to the ‘countPartitions()' function. This function will return the number of partitions we can make.
If partitions > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.
'''

'''
Intuition
When you first see this problem, your brain might try to find the exact splits. You might think, "Should I try splitting here? Or here? What if I use dynamic programming?" This can feel overwhelming because the number of ways to split an array is huge.

The mental trick is to stop trying to find the answer directly.

Instead, change the question. Ask a much simpler, "Yes/No" question:

"If I set a maximum allowed sum (let's call it X), can I split the array into k bags (or fewer)?"

This question is much easier to answer. You can just be "greedy":

Start with your first bag.

Keep stuffing numbers into it.

As soon as the next number won't fit without going over the X limit, close that bag and start a new one.

At the end, count how many bags you used. If bags_used <= k, the answer is "Yes!"

This "Yes/No" function is exactly what our canFit helper method does.

Now, think about the possible answers for X:

If you can't do it with a limit of X = 17, you definitely can't do it with X = 16, X = 15, etc.

If you can do it with a limit of X = 18, you definitely can do it with X = 19, X = 20, etc. (a bigger bag only makes it easier).

This creates a "sorted" range of answers: [No, No, No, No, Yes, Yes, Yes, Yes]

We are looking for the very first "Yes". This is a perfect job for Binary Search.

Approach
Define the Search Space: We need to find the smallest possible "largest sum."

What's the lowest possible answer? The largest single number in the array. We at least need a bag big enough to hold that one item. (This is our min or low boundary).

What's the highest possible answer? The sum of the entire array. This is the case where k=1 and we put everything in one giant bag. (This is our max or high boundary).

Binary Search: We will search for our answer in the range [low, high].

We pick a mid value from this range. This mid is our "guess" for the maximum allowed sum.

We ask our helper function: canFit(nums, mid, k). This translates to: "Hey, can we split the array if no bag is allowed to be larger than mid?"

Adjust the Search:

If canFit returns true: This mid is a possible answer. But maybe there's an even smaller one that also works. So, we save this answer (soln = mid) and try to find a better one by searching in the left half (max = mid - 1).

If canFit returns false: Our mid guess was too small. The bags weren't big enough, and we used too many. We must allow for larger bags. We search in the right half (min = mid + 1).

The canFit Helper Function:

This is our greedy "bag-filler" function.

Start with count = 1 (the first bag) and sum = 0.

Loop through each num:

If sum + num is larger than our limit (perK, which is the mid from our binary search), we must "close" this bag.

Increment the bag count and start the new bag with sum = num.

Otherwise, the number fits! Just add it to the current bag's sum.

Finally, return count <= k. This tells our binary search if the "guess" worked.

The loop continues until min crosses max, and soln will hold the smallest value for mid that ever returned true.

Complexity
Time complexity: O(n log(S))
n is the length of the nums array.
S is the sum of all elements in nums.
The Binary Search runs in O(log(S)) steps (because our search space is from low to high, where high is S).
Inside each step of the binary search, we call canFit, which loops through the entire array. This takes O(n) time.
Total: O(n)⋅O(log(S)) = O(n⋅log(S)).
Space complexity: O(1)
We only use a few extra variables (min, max, soln, mid, count, sum) to store simple numbers.
We don't use any extra arrays, data structures, or recursion that depends on the input size.

'''

class Solution:
    def paint(self, A: int, B: int, C: list[int]) -> int:
        # Your code goes here
        def is_possible(sumi):
            sub = 1
            run_sum = C[0]
            for i in range(1,len(C)):
                if run_sum+C[i]>sumi:
                    sub+=1
                    run_sum = C[i]
                else:
                    run_sum+=C[i]
            return sub

        low = max(C)
        high = sum(C)
        while(low<=high):
            mid = (low+high)//2
            if is_possible(mid)<=A:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return (ans*B)%10000003

        