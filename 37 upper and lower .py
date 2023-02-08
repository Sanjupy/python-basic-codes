def find_string(s): #function for find string
    d={"upper_case":0,"lower_case":0} #first give upper and lower strings as 0 
    for i in s: #looping the string(s)
        if i.isupper(): #if i is upper
            d["upper_case"]+=1 #increment the upper case
        elif i.islower():
            d["lower_case"]+=1 #increment lower case
        else:
            pass
print (find_string("sanjeev KuMMAR"))



        

