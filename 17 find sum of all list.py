#sum all numbers in a list
def sum(numbers):#function defination
    total=0#local variable
    for x in numbers:#numbers=[1,2,3,4,5]
        total=total+x#1st iter 0=0+1,2nd iter 0=1 +2=3,3rd iteris 3+3=6,6+4=10
    return total#1 will go to total=1,2...total is 10 it return so total is 10
print(sum([1,2,3,4]))#this will go to function defination

