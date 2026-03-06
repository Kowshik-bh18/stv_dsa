from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)

        left = 0
        formed = 0

        window = {}
        res = [-1,-1]
        min_len = float('inf')

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char,0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:

                if (right-left+1) < min_len:
                    min_len = right-left+1
                    res = [left,right]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        l,r = res
        return "" if min_len == float('inf') else s[l:r+1]
    
#another solution to reduce two hashmap

def anot():

        start = -1
        min_length = float('inf')
        has = defaultdict(int)
        l = 0
        count=0
        for k in t:
            has[k]+=1
        for r in range(len(s)):
            if has[s[r]]>0:
                count+=1
            has[s[r]]-=1
            while(count==len(t)):
                if(r-l+1<min_length):
                    min_length = min(min_length,r-l+1)
                    start=l
                has[s[l]]+=1
                if has[s[l]]>0:
                    count-=1
                l+=1
        if start==-1:
            return ""
        return s[start:start+min_length]