def is_prime(number):
    if number>1:#5>1
        for num in range(2,number):#2,3,4 
            if(number%num==0):#first iter 5%2==0 false so return prime 2nd iter 5%3==0 false so return prime and so on
                return "not prime"
        return "prime"
    return "not a prime"
print(is_prime(5))
