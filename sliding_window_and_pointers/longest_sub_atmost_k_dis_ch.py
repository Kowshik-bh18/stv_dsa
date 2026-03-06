class Solution:
    def kDistinctChar(self, s, k):
        #your code goes here
        left=0
        hash_map = {}
        maxi_len = 0
        for right in range(len(s)):
            hash_map[s[right]]=hash_map.get(s[right],0)+1
            while len(hash_map)>k:
                hash_map[s[left]]-=1
                if hash_map[s[left]]==0:
                    del hash_map[s[left]]
                left+=1
            
            maxi_len = max(maxi_len,right-left+1)
        return maxi_len
    
'''
Instead of checking all substrings, we can use a sliding window and maintain the count of characters in the current window using a frequency map. The idea is to expand the window to the right as long as we have at most K distinct characters. If the count exceeds K, we shrink the window from the left until we’re back within the limit. This avoids unnecessary re-checks and speeds up the solution.
Initialize two pointers to define the sliding window: one at the start and one at the end.
Use a hashmap to track the frequency of each character within the window.
Expand the window by moving the right pointer forward.
If the number of distinct characters exceeds the limit, shrink the window from the left.
At every valid window, update the maximum length found so far.
Continue until the end of the string is reached.


Complexity Analysis

Time Complexity:O(n) ,We iterate through the string once, and each character is added and removed from the map at most once. So the overall time complexity is linear.

Space Complexity: O(k) ,We store at most k characters in the frequency map at any given time, so space used is proportional to k.
'''