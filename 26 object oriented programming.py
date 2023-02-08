class student:

    name="sanjeev"#global variable 
    def __init__(self,age,number):
        self.age=3
        self.number=1234

student1=student(3,1234)
print(student1.age)
print(student1.name) #we can call the name without calling it in local variable
print(student1.number)

