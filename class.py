class Person:
    des="nothing"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print("my name is {} and I am {} years old".format(self.name,self.age))

    def eat(self,food):
        print("{} eats {} ".format(self.name,food))

    def action(self):
        print("{} jumps ".format(self.name))


    





class Baby(Person):
    

    def speak(self):
        print("bababbabbaba")
        

    def nap(self):
        print("{} take a nap ".format(self.name))





p1=Person("ankit",40)
p1.speak()
p1.eat("pasta")
p1.action()
print(p1.des)


b1=Baby("satya",6)

b1.speak()
b1.eat("babyfood")
b1.action()
print(b1.des)





