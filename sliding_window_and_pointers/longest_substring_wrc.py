class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash_map = {}
        max_len=0
        for right in range(len(s)):
            while s[right] in hash_map:
                hash_map.remove(s[left])
                left+=1
            hash_map[s[right]]=right
            max_len = max(max_len,right-left+1)
        return max_len


#optimized solution


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash_map = {}
        max_len=0
        for right in range(len(s)):
            if s[right] in hash_map:
                if hash_map[s[right]]>=left:
                    left = hash_map[s[right]]+1
            hash_map[s[right]]=right
            max_len = max(max_len,right-left+1)
        return max_len


#logical intuition
'''
✅ Algorithm 

Start with two pointers: left = 0 and iterate right from 0 to end of string.

Use a hashmap to store the last index of each character.

If the current character is already seen inside the current window, move left to one position after its last occurrence.

Update the character’s latest index in the hashmap.

At each step, calculate window length (right - left + 1) and update the maximum length.

⏱ Time Complexity

O(n)

Reason:

Each character is visited at most twice (once by right, once by left).

No nested loops.

So total operations are proportional to string length.

🗂 Space Complexity

O(min(n, m))

Where:

n = length of string

m = number of unique characters (at most 128 for ASCII)

Worst case:
If all characters are unique → hashmap stores all characters → O(n).
'''

#we can also solve this problem just by using set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        count = set()

        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left+=1

            count.add(s[right])

            max_length = max(len(count),max_length)

        return max_length
            


        