class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and (n&(n-1))==0:
            return True
        return False
    
'''
trick:-

power of 2 has one bit set so if w do & n-1 then n-1 makes that bit zero and all other 1 so on computing
 n&(n-1) if we get 0 then it is power of 2 otherwise it not 


 we can use built in function bin(number).count('1') if it is 1 then true otherwise false
'''
        