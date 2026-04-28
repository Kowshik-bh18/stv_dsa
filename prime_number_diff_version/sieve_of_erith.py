#1
n=30
is_prime = []
for i in range(n+1):
    is_prime.append(1)
for i in range(2,n+1):
    if(is_prime[i]):
        for j in range(i+i,n+1,i):
            is_prime[j]=0
print(is_prime)

for i in range(2,n+1):
    if is_prime[i]:
        print(i,end="->")


#2
'''
we can slightly optimze above because instead of starting j in loop from i+i we can start from i*i
lets look for an example

2x2=4   3x2=6    5x2=10
2x3=6   3x3=9    5x3=15
2x4=8   3x4=12   5x4=20
2x5=10  3x5=15   5x5=25


if we observe upto 3X3 it is alrdy marked by 2 since it also has same multiple 

also if we observe 5 upto 5X5 it is lardy marked by 2 and 3 since multiple 

so we can start from i*i

'''

n=30
is_prime = []
for i in range(n+1):
    is_prime.append(1)
for i in range(2,n+1):
    if(is_prime[i]):
        for j in range(i*i,n+1,i):
            is_prime[j]=0
print(is_prime)

for i in range(2,n+1):
    if is_prime[i]:
        print(i,end="->")

#3
'''
if we observe it is ok if we move puter loop untile sqrt(n) because if we do i*i then it will go beyund this if we 
go next from sqrt(n)

example 5x5 = 25
        6x6->out of range so we can go upto sqrt(n)
'''

n=30
is_prime = []
for i in range(n+1):
    is_prime.append(1)
for i in range(2,int(n**0.5)+1):
    if(is_prime[i]):
        for j in range(i*i,n+1,i):
            is_prime[j]=0
print(is_prime)

for i in range(2,n+1):
    if is_prime[i]:
        print(i,end="->")

'''

Time Complexity: O(n log log n)
Space Complexity: O(n)

🔹 Rough feel with numbers
n	log n	log log n
100	~4.6	~1.5
10⁶	~13.8	~2.6
10⁹	~20	~3

👉 See? log log n grows very slowly

🔹 Final takeaway (interview-ready)

Say this:

“Each prime marks about n/p multiples, and the sum of reciprocals of primes is log log n, so total complexity becomes O(n log log n).”
'''