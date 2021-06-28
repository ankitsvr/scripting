class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=name
        self.weight=weight

    def introduce(self):
        print("My name is " + self.name)

class Person:
    def __init__(self,n,b,i):
        self.name=n
        self.behavior=b
        self.is_sitting=i


r1=Robot("ankit","black",24)


p1=Person("satya","calm", False)


p1.robot_own=r1
p1.robot_own.introduce()
