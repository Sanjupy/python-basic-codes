#2000 is a leap year
def checkyear(year):#this is the function #2000
    return ((year%4==0)and(year%100!=0)) or (year%400==0) #2000%4==0(true i.e 1) 2000%100!=0(false i.e 0 )0 and 1 is 0 i.e (false) or (2000%400==0 this is true i.e 1) so 0 or 1 is 1 that is true .condition is true
year=2000 #this year (2000) goes to function call(1st statement)
if (checkyear(year)):#year is taken in if condtion ,this condition satisfies 
    print("leap year")
else:
    print("not a leap year")
