def is_prime(number):#this is function
    if number>1:#prime number should be greater than 1 
        for num in range(2,number):#prime starts with 2 so (2,number=11)(2,11)
            if(number%num==0):
                return "not prime"
        return "prime"
    return " not prime" #if num is not greater than 1 return not a prime eg : if number is zero
print(is_prime(9))
