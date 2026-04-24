class Solution:
    def setBit(self, n):
        if (n & (n + 1)) == 0:
            return n
        return n | (n + 1)
    
'''
here | preserves other bits valid and n+1 fins correct position

'''