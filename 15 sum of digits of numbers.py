n=int(input("enter the number"))

sum1=0

while(n>0):#145,14,1
    rem=n%10#5,14%10=4,1%10=1
    sum1=sum1+rem#5,4,1
    n=n//10#145//10,14//10=1
print("the sum of digits is ",sum1)