class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        i = 0
        start_ind = -1
        min_len = float('inf')

        while i < n:
            j = 0

            # forward scan
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:
                        break
                i += 1

            if j < m:
                break

            end = i
            j = m - 1

            # backward scan
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            i += 1

            if end - i + 1 < min_len:
                min_len = end - i + 1
                start_ind = i

            i += 1

        return "" if start_ind == -1 else s1[start_ind:start_ind + min_len]
    

'''
Find subsequence  → O(n)
Shrink window     → O(m)
Repeat ≤ n times

Time  : O(n × m)
Space : O(1)
'''