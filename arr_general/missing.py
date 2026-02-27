'''
approach 1:-
we can use sum of n natural number formula that is n*(n+1)//2 which is subtarted with sum of array form this we
will get missing number

approach 2:-
 XOR of a number with itself is 0 i.e. x ^ x = 0 and the given array arr[] has numbers in range [1, n]. 
 This means that the result of XOR of first n natural numbers with the XOR of all the array elements will be the missing number. To do so, calculate XOR of first n natural numbers and XOR of all the array arr[] elements, and then our result will be the XOR of both the resultant values.
'''


arr =[1,2,3,5,6,7,8]
n = len(arr)
xor1=xor2=0
for i in range(n):
    xor1^=arr[i]
for i in range(1,n+2):
    xor2^=i
print(xor1,xor2)

print(xor1^xor2)


# this xor behaviour helps in many optimization tricks