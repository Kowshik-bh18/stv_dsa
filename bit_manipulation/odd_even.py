class Solution:
    def isOdd(self, n: int) -> bool:
        # Your code goes here
        if n&1:
            return True
        return False
    
'''
trick

last bit of odd number -1
last bit of even number - 0

if we do and operation with 1 

then if the number is odd then it yield 1

else it yields 0
'''