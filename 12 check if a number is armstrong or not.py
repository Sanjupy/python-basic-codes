n=int(input("enter the number:"))#153 is armstrong
sum1=0#initially sum is zero
temp=n#371 is stored in temporary variable
while(n>0):#153>0,15>0,1>0
    rem=n%10 #153%10=3,15%10=5,1%10=1
    sum1=sum1+rem**3#3**3=27,5**3=125,1**3=1
    n=n//10#153//10=15,15//10=1

if(temp==sum1):
    print("is armstrong")
else:
    print("not armstrong")

