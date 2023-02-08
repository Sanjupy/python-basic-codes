n=int(input("enter a number:"))
print("the reverse number is ",end="")
while(n!=0):
    rem=n%10 
    print(rem,end="")
    n=n//10
