# this is same as hamming distance(no of bits that are different)

'''
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

 

Example 1:

Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
Example 2:

Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x^y).bit_count()
        


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # b_s = format(start,'b')
        # b_g = format(goal,'b')
        # l_s,l_g = len(b_s),len(b_g)
        # if l_s!=l_g:
        #     if l_s>l_g:
        #         b_g = ('0'*(l_s-l_g)) + b_g
        #     else:
        #         b_s = ('0'*(l_g-l_s)) + b_s
        # min_flips = 0
        # for i,j in zip(b_s,b_g):
        #     if i!=j:
        #         min_flips+=1
        # return min_flips


        #easy solution

        '''based on the fact that xor makes even no of bits which means same bits   zero and remaining one '''

        return (start^goal).bit_count()



        
            
        
        