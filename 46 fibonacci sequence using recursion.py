#python programme tos olve fibonocii series
#formula fib(n-1)+fib(n-2)
def fib(n):#function is given
    if n==1 or n==2:#if n value is 1 or 2 return 1 value as fib(1-1)+fib(1-2 )returns one simalr with n=2 also
        return 1
    else:
        return(fib(n-1)+fib(n-2))#fib(3)=3-1=2,where fib(2)is 1 +and fib(3-2)is 1 so 1+1=2 so the fib(3)is 2 
print(fib(3))#it goes to the function as fib(7) is not 1 or 2 it goes to else statement
#fib(7)=the 7 th element value will be taken into account for example:
#0=first term and 1 is second term=0+1=1 ,then 1 is thrid now 1+1=2 ,2 is fourth term and so on 
#0,1,1,2,3,5,8,13 there fore the fib(7) is 13 as 7 th index is 13

#fib(7),6+5

    