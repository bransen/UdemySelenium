#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructor etc

class Calculator:
    num = 100 #class variable
#Default Constructor
    def __init__(self, a, b):
        self.a= a
        self.b= b
        print("I am printed automatically when an object created")
    def getData(self):
        print("I am now executing as a method in a class")

    def Summation(self):
        return self.a + self.b + Calculator.num



obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.num)

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.num)