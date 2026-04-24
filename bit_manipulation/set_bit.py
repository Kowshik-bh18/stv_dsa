'''
Check if the i-th bit is Set or Not
Subscribe to TUF+

Hints
Company
Given two integers n and i, return true if the ith bit in the binary representation of n (counting from the least significant bit, 0-indexed) is set (i.e., equal to 1). Otherwise, return false.


Example 1

Input: n = 5, i = 0

Output: true

Explanation: Binary representation of 5 is 101. The 0-th bit from LSB is set (1).



Example 2

Input: n = 10, i = 1

Output: true

Explanation: Binary representation of 10 is 1010. The 1-st bit from LSB is set (1).
'''

class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        # Your code goes here
        if (n & (1<<i))!=0:
            return True
        return False


'''
1<<i  create the mask by setting only ith bit 

which means it will keep only ith bit 1 and others zero 


when we do and operation with number and 1<<i  if ith bit in number is 1 then it will result in number which is not equla to zero

otherwise the above operation will become zero

lets take 7

111

1<<1

001

111 & 010

it will result in non zero number

'''