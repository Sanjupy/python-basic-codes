#find the largest number among three inputs
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if(num1>=num2) and (num1>=num3): #both statements should be satisfied
    print("num1 is the largest")
elif (num2>=num1) and (num2>=num3): #both statements should be satisfied
    print("num2 is the largest")
else:                             #if above both wont get satisfied else statement will be satisfied
    print("num3 is the largest")
