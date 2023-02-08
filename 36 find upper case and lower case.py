def check_String(s):
    d={"upper_case":0,"lower_case":0}
    for i in s:
        if i.isupper():
            d["upper_case"]+=1
        elif i.islower():
            d["lower_case"]+=1
        else:
            pass
    print("upper case",d["upper_case"])
    print("lower",d["lower_case"])
print(check_String("sanjeev KUMAR"))
