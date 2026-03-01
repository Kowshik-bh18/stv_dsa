#below solution is the smart way of counting substrings without checking every substrings

'''
Instead of checking every possible substring, we use the sliding window technique. We maintain a window [left, right] such that it contains at least one of each character 'a', 'b', and 'c'. Once we get such a window, any substring that starts at or before left and ends at right will also be valid. So we can add left + 1 to the result for each valid right. This avoids rechecking every substring and reduces unnecessary checks.
Initialize a result counter to store the total number of valid substrings.
Maintain a hash map or frequency array to track the count of each character 'a', 'b', and 'c' in the current window.
Initialize a left pointer to 0. We'll use it to track the start of the sliding window.
Iterate through the string using a right pointer from 0 to the end of the string
For each character at the right pointer, increment its count in the frequency map.
'''



class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash_map = {'a':-1,'b':-1,'c':-1}
        count = 0
        for i in range(len(s)):
            hash_map[s[i]]=i
            # if hash_map['a']!='-1' and hash_map['b']!=-1 and hash_map['c']!=-1:
            count= count+min(hash_map.values())+1
        return count

        