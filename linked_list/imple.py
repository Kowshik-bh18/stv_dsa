class DbLinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
node = DbLinkedList(10)
l = [1,2,3,4,5,6]
temp1=temp2 = node

for i in l:
    new_node = DbLinkedList(i)
    temp1.next = new_node
    new_node.prev = temp1
    temp1 = new_node
while temp2.next!=None:
    print(temp2.val,end="->")
    temp2=temp2.next
print("last pointer position:")
while temp2.prev!=None:
     print(temp2.val,end="->")
     temp2=temp2.prev
