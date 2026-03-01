'''
The key optimization over the previous sliding window method is to avoid shrinking the window. Instead of always adjusting the window size based on the replacement condition, we keep expanding the window as long as the current window satisfies the condition. We don’t need to shrink the window manually because the maximum window size that satisfies the constraint can be tracked directly, as we are only asked for the maximum length, not the actual substring.

hence, as we slide the window, we always try to increase the window size. We maintain the count of the most frequent character in the current window. If the difference between the window size and this count exceeds k, it means we need more than k replacements but instead of shrinking, we just continue checking and computing the maximum valid length encountered.

This approach avoids recalculating the maximum frequency on every iteration, making it faster than the better approach.
Initialize a frequency array or hashmap to store character frequencies in the current window.
Track the count of the most frequent character seen so far in the window.
For every character, expand the window by moving the right pointer.
If (current window length - max frequency) exceeds k, it means more than k replacements are needed, so we move the left pointer forward.
Throughout the loop, update the max window length that satisfies the constraint.
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_freq = max_len = left = 0
        for right in range(len(s)):
            if s[right] in hash_map:
                hash_map[s[right]]+=1
            else:
                hash_map[s[right]]=1
            max_freq = max(max_freq,hash_map[s[right]])
            if (right-left+1)-max_freq >k:
                hash_map[s[left]]-=1
                left+=1
            if (right-left+1)-max_freq <=k:
                max_len = max(max_len,right-left+1)
        return max_len

'''
Time Complexity: O(n), where n is the length of the string,each character is processed at most twice once by the right pointer, once by the left. All operations inside the loop run in constant time.

Space Complexity: O(1), constant space .Only a fixed-size frequency array (26 letters) is used, regardless of input size.
'''
        