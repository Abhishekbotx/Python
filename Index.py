print("heloo")

if 5>2:
    print('true')


#unpacking a collection ---> destructuring in js

fruits=['banana','orange','apple']
x,y,z=fruits

# print(x,y,z)

for x in fruits:
  print('fruit:',x)



#slicing in python

b = "Hello, World!"
print(b[2:5]) #this will slice from index 2 to 

# the trim methlod is actually strip method in pythong


#loop through at dictionary:: dictonary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)


#positive only arguments



#To specify that a function can have only positional arguments, add , / after the arguments:


def my_function(x, /):
  print(x)

my_function(3)

b=[fruits]


def fruit_salad(fruit):
  for x in fruit:
    print('food:', x)

fruit_salad(fruits);        


class myClass:
  x=5*3

new=myClass()
print('class result',new.x)  


# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:


# 🧠 Python Class vs JavaScript Class: Understanding self
# In Python:

class Person:
  def __init__(self,name,age,gender,salary):
    self.name=name
    self.age=age
    self.gender=gender
    self.salary=salary

  def __str__(self):
    return f"{self.name} {self.age} {self.salary}"


P1=Person('Abhishek',23,'M',00000)  
print(P1)  
# print('p1 here:',P1.name,P1.age,P1.gender,P1.salary)


# self is just a convention in Python that refers to the instance of the class.
# It’s like this in JavaScript.
# When you define a method inside a class, Python automatically passes the object (self) as the first argument when you call the method.


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


"If the __str__() function is not set, the string representation of the object is returned,"

# …it means Python will return the default memory-based representation, which is something like:
# <__main__.Person object at 0x000001A3B8F739A0>


#🌟 Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:


class Person:
  def __init__(thisOne,name, age):
     thisOne.name=name 
     thisOne.age=age 

  def myFunc(per):
    print('My name is:',per.name,'and i am ',per.age,'young')  

human=Person('Abhi',23)     

human.myFunc() 
# del human.age this will dlete the property

print(human.age)