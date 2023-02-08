#global variables outside the function
#local variables inside the function 
class student:

    m="mangu"#global variable called before function
    def __init__(self,name,age,address):
        self.name="sanju"
        self.age=21
        self.address="india"

student1=student("sanju",21,"india")

print(student1.name)#local variable
print(student1.age)
print(student1.address)
print(student1.m)#global variable

