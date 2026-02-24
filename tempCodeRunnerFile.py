#follow below pattern for right rotation

'''
assume roation as two parts a+b 
a->should go to b side and b-> should go to a side 

so simple way is 

1. rotate entire array now it becomes reverse(b) + reverse(a)

2. correct the individual part-> reverse b and reverse a 

note:- use modulus to avoid unnecessary rotation
'''
l=[1,2,3,4,5]
k = 2
def reverse(arr,left,right):
    while(left<right):
        arr[left],arr[right] = arr[right],arr[left]
        right-=1
        left+=1
k %=len(l)
reverse(l,0,len(l)-1)
reverse(l,0,k-1)
reverse(l,k,len(l)-1)
print(l)

