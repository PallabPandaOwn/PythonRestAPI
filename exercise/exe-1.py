#list , Tuple , Set

# List Comprehensions

friends = ['A', 'B','C']

result = [friend for friend in friends if friend.startswith('A')]
print(result)

# Dictionaries
dis = {'A':'30'}

# Destructure variables

x, y = 2, 3 
print(x, y)

# Functions

def Hello():
    print('hello')

Hello()

def add(x,y):
    print(x+y)

add(2,y=3)


# Class

class Student():
    def __init__(self,name,grades):
        self.name =name
        self.grades = grades

    def avg_grades(self):
        return sum(self.grades)/len(self.grades)


std1 = Student('Pallab',(10,30,40))
print(f'Name of student - {std1.name} and Grades - {std1.grades}')
print(std1.avg_grades())


# class school(Student):
#     super()

# --------------------#

def fun(seq: int)-> int:
    return seq

print(fun(5))

# --------#
import sys 
import mymodule

mymodule.add(1,2,3)

print(__name__)

def divide(divident:int,divisor:int)-> float:
    result=divident/divisor
    print(result)

try:
    divide(6,0)
except ZeroDivisionError as e:
    print('divisor canot be zero')

