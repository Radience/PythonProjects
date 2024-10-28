
"""
txt = "know knew hold the station green"
print(txt[txt.find("hold"):txt.find("hold")+len("hold")] + "\n" + str(txt.find("hold")) + " " + str(txt.find("hold")+len("hold")))
print(txt.find("know"))
print(txt[0:4])
"""
"""
exampleFirstText = "#^$#&$"
print(exampleFirstText.isalnum())
listExample = ["one", "two", "three", "four"]
print(listExample[2])
tList = ["one", "two", "three", "abs", "bbs", "cbs"]

for x in range(2,5):
    print(tList[x])
"""
"""
thisDictionary = {
"brand" : "Suzuki",
"model" : "",
"year" : ""
}

print(thisDictionary)

thisDictionary["color"] = ["red", "blue", "green"]
thisDictionary["brand"] = int("123")
print(thisDictionary)
thisDictionary["brand"] = thisDictionary["brand"] - 3
print(thisDictionary)

if thisDictionary["brand"] == 120:
    print("Yes, its here")
"""

"""def BeforeFunction(b):
    return lambda a : a * b

lmb = BeforeFunction(10)

print(lmb(5))"""

"""class Person: #Base class
    def __init__(self, name, sname, age):
        self.Firstname = name
        self.Lastname = sname
        self.Age = age

    def printname(self):
        print(self.Firstname, self.Lastname, self.Age)

class Student(Person):
    def __init__(self, name, sname, age, numberSchool):
        super().__init__(name, sname, age)
        self.NumbSchool = numberSchool

    def printStudent(self):
        print(self.Firstname, self.Lastname, self.Age, self.NumbSchool)



name = input("Your name: ")
sname = input("Your second name: ")
age = input("Your age: ")
numbeSchool = input("Your School: ")
Student(name, sname, age, numbeSchool).printStudent()"""

"""class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

for x in (Car("car", "super"), Boat("boat", "slow"), Plane("plane", "high")):
    x.move()"""

"""import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))"""

"""import json

x = '{"name":"John","age":30,"city":"NY"}'

y = json.loads(x)

print(y["age"])

x = {
    "name" : "John",
    "age" : 30,
    "city" : "NY"
}

y = json.dumps(x)
m = json.loads(y)
print(m["age"])"""
"""
word = 2

if type(word) is not int:
    raise TypeError("Only integers are allowed")

if type(word) is not str:
    raise TypeError("Only string are allowed")"""

"""
def hello(func):
    def inner():
        print("Hello ")
        func()
    return inner

def name():
    print("Alice")


obj = hello(name)
obj()"""

import random

class MyCircularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        if((self.tail + 1) % self.size == self.head):
            print("The queue is full\n")
        elif (self.head) == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail +1) % self.size
            self.queue[self.tail] = data

    def dequeue(self):
        if(self.head == -1):
            print("The queue is empty\n")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp

    def printqueue(self):
        if(self.head == -1):
            print("Is empty, i cant print\n")

        elif(self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(i, end = " ")
            print()
        else:
            for i in range(self.head, self.size):
                print(i, end = " ")
            for i in range(0, self.tail + 1):
                print(i, end = " ")
            print()

que = MyCircularQueue(5)
for x in range(que.size):
    que.enqueue(random.randint(1, 10))
print("Before Delete: ")
que.printqueue()
print("After Delete: ")
que.dequeue()
que.printqueue()
print("After additional number:")
que.enqueue(47)
que.printqueue()
