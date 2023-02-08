#153=351
n=int(input("enter the number:"))
sum1=0
temp=n
rev=0
while(n>0):#153,15,1
    rem=n%10#153%10=3,15%10=5,1%10=1
    rev=rev*10+rem#351
    n=n//10#153//10=15,15//10=1,          stop as zero came1//10=0
if(temp==rev):
    print("palindrome")
else:
    print("not")
