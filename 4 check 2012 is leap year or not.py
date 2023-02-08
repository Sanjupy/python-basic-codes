#2012
def checkyear(year):#this is function #the year=2012 comes here and checks return statement and goes to if statement
    return(year%4==0 and (year%100!=0))or (year%400==0)#year=2012 one condition must be true (and condition is 1 and or is 0) 1 and 0 is 1 so true
year=2013
if checkyear(year):
    print("it is leap year")
else:
    print("not a leap year")


