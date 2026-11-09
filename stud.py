import random
class student:
    def __init__(self,name,age):
        self.year=2026
        self.section="A"
        self.id=random.randint(10,99)
        self.student_id=str(self.year)+self.section+ str(self.id)
        self.name=name
        self.age=age
        
    def display(self):
        print(self.student_id)
        print(self.name,self.age)
name=input("enter name :")
age=int(input("enter age:"))        
s=student(name,age)
s.display()
