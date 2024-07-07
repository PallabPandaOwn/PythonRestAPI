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
print(f'Name of student - {std.name} and Grades - {std.grades}')
print(std.avg_grades())


# --------------------#

