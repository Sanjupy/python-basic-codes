n=int(input("enter the numbeer"))
sum1=0
temp=n
while(n>0):
    rem=n%10
    sum1=sum1+rem**3
    n=n//10
#27+125+
if(temp==sum1):

    print("armstrong")
else:
    print("not")