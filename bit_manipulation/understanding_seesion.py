def decimal_to_binary(num):
    no = ""
    while num>1:
        rem = num%2
        no+=str(rem)
        num = num//2
    no+="1"

    print(no[::-1])
decimal_to_binary(7)
