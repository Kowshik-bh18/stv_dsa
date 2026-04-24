class Solution:
    def countSetBits(self, n: int) -> int:
        # Your code goes here
        setbits = 0
        while n>0:
            if n&1:
                setbits+=1
            n>>=1
        return setbits
    
'''
counting by elemenating rightmost bit one by one 
otherwise sue built in function bin(number).count('1')
'''

#optimal

def count_set_bits(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


'''
n & (n - 1) removes the RIGHTMOST set bit

Each loop = one set bit removed

🧠 Let’s See It in Action
🧪 Example
n = 10   # binary: 1010
🔍 Iteration 1
n     = 1010
n - 1 = 1001
1010
1001
----
1000

👉 New n = 1000
👉 One set bit removed
👉 count = 1

🔍 Iteration 2
n     = 1000
n - 1 = 0111
1000
0111
----
0000

👉 New n = 0
👉 count = 2

🎯 Final Answer
Set bits = 2
💡 Why does this work?

Let’s understand the pattern

🔍 General Form
n = xxxx1000...000
        ↑
    rightmost 1
Now n - 1
n - 1 = xxxx0111...111

👉 That rightmost 1 becomes 0
👉 All bits to the right become 1

Now AND
n       = xxxx1000...000
n - 1   = xxxx0111...111
------------------------
result  = xxxx0000...000

👉 That last 1 disappears

🔥 Key Insight
Each operation removes ONE set bit

So:

Number of iterations = number of 1s

'''