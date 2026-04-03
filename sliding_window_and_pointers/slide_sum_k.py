#r-1
l = [10,5,2,7,1,9]
j = 0
max_len = 0
sumi = 0
k = 15

for i in range(len(l)):
    sumi += l[i]
    
    while sumi > k:
        sumi -= l[j]
        j += 1
    
    if sumi == k:
        max_len = max(max_len, i - j + 1)

print(max_len)


'''
Algorithm
Two pointers, left and right, are used to maintain the current window of elements in the array. These pointers represent the start and end of the current subarray.
A variable, sum, is used to keep track of the sum of the elements in the current window between left and right.
The right pointer expands the window by including new elements, increasing the sum.
If the sum of the window exceeds k, the left pointer shrinks the window by removing elements from the start until the sum is less than or equal to k.
If the sum of the current window equals k, the maximum length of such a subarray is updated.
The process continues until the right pointer traverses the entire array.
Finally, the maximum length of the subarray with sum k is returned as the result.


⏱ Time Complexity
👉 O(n)
Why?

Even though you have:

one for loop

one while loop inside

It is NOT O(n²).

🧠 Important Understanding

i moves from 0 → n-1 (n times)

j also moves from 0 → n-1 (at most n times)

Each element:

is added to sumi once

is removed from sumi once

So total operations ≈ 2n

O(n+n)=O(n)
⚡ Why It Is Not O(n²)?

Because:

j never resets to 0

It only moves forward

Each element is processed at most twice

This is called amortized linear time.

📦 Space Complexity

👉 O(1)
Because you are using only variables (no extra data structures).

🎯 Final Answer

Time Complexity: O(n)

Space Complexity: O(1)

Optimal for positive numbers
'''


# to handle negative number we cant proceed with above logic 

# so we proceed with prefix sum + hashmap

def all_cond():
    hashmap = {}

    prefix_sum = 0

    for i in range(len(nums)):
        prefix_sum+=nums[i]

        if prefix_sum==k:
            max_len = i+1
        if (prefix_sum-k) in hashmap:
            length = i-hashmap[prefix_sum-k]
            max_len = max(max_len,length)
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i
    return max_len

'''
🎯 We Want

Length of subarray whose sum = k

We use this idea:

𝑐
𝑢
𝑟
𝑟
𝑒
𝑛
𝑡
_
𝑠
𝑢
𝑚
−
𝑝
𝑟
𝑒
𝑣
𝑖
𝑜
𝑢
𝑠
_
𝑠
𝑢
𝑚
=
𝑘
current_sum−previous_sum=k

Now your doubt:

Why does i - previous_index give correct length?

Let’s break it carefully.

🟢 Step 1: What Does Prefix Sum Mean?

At index i:

𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑖
]
=
𝑠
𝑢
𝑚
(
0
→
𝑖
)
prefix[i]=sum(0→i)

At index j:

𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑗
]
=
𝑠
𝑢
𝑚
(
0
→
𝑗
)
prefix[j]=sum(0→j)
🟢 Step 2: How To Get Subarray Sum?

Suppose we want sum from:

j+1 → i

That sum equals:

𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑖
]
−
𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑗
]
prefix[i]−prefix[j]

Why?

Because:

(
0
→
𝑖
)
−
(
0
→
𝑗
)
=
(
𝑗
+
1
→
𝑖
)
(0→i)−(0→j)=(j+1→i)

This is the key idea.

🟢 Step 3: Connect To Our Condition

We want:

𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑖
]
−
𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑗
]
=
𝑘
prefix[i]−prefix[j]=k

Rearranging:

𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑗
]
=
𝑝
𝑟
𝑒
𝑓
𝑖
𝑥
[
𝑖
]
−
𝑘
prefix[j]=prefix[i]−k

So if:

prefix[i] - k

exists earlier at index j,
then subarray from j+1 to i has sum = k.

🟢 Step 4: Why Length = i - j ?

Subarray starts from:

j+1

Ends at:

i

Length formula:


i−(j+1)+1

Simplify:

That’s why we use:

i - previous_index
🔎 Let’s See With Real Example
arr = [1, 2, 3, 1, 1, 1]
k = 3

We calculated earlier:

At index 5:

prefix_sum = 9

We check:

prefix_sum - k = 9 - 3 = 6

6 existed earlier at index 2.

So:

j = 2
i = 5

Subarray is:

j+1 → i
3 → 5

That subarray:

[1,1,1]

Length:

5
−
2
=
3
5−2=3

Correct ✅

🟢 Visual Understanding

Think like this:

Index:   0  1  2  3  4  5
Array:   1  2  3  1  1  1
Prefix:  1  3  6  7  8  9

At index 5:

prefix = 9

We find earlier prefix = 6 at index 2.

So we remove sum up to index 2.

What remains?

From index 3 to 5

Which is exactly what we want.

🧠 Core Intuition (Very Important)

When we find:

prefix[i] - k

That means:

There was some earlier point where total sum was smaller by k.

So everything between those two points must add up to k.

🟢 Why It Works Even With Negative Numbers

Because subtraction logic does not depend on order.

It purely depends on:

prefix[i]−prefix[j]

Which is mathematically correct always.

'''