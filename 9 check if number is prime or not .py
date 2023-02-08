#prime numbers should be greater than 1 
#factor should be 1 and itself eg 5 5*1 and not 6 as 3*2 
def is_prime(number):
    if number>1:#6>1
        for num in range(2,number):#num=2,3,4,5
            if number%num==0: #6%2==0 not a prime if false return prime
                return "not a prime"
        return "prime"
    return "not a prime"  #if num is not greater than 1 return not a prime eg : if number is zero
print(is_prime(5))

    