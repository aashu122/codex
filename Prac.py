#Python Version
"""
import sys
print("Python Version")
print(sys.version)
print(sys.version_info)
"""
"""
#Date And Time
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
"""
"""
from math import *
def Area(r):
    return pi*r*r
a = Area(5)
print("Area of circle is %0.2f"%a)
"""
"""
def rev(f,l):
    return l,f
a = rev("ashu","pandey")
print(a)
"""
"""
lst = []
for i in range(0,5):
    print("Enter a Number"+str(i+1)+":")
    x = int(input())
    lst.append(x)
print("The list is:",lst)
"""
"""list =  ["Red","Green","White" ,"Black"]
for i in range(len(list)):
    if i == 0:
        print(list[0],end =" ")
    elif i == len(list)-1:
        print(list[-1])
"""
"""import datetime
exam_st_date = (11,12,2014)
print("%i / %i / %i"%exam_st_date)
"""
# Add n+nn+nnn
"""
num =int(input("Enter a Number:"))
i = int("%s"%num)
j = int("%s%s"%(num,num))
k = int("%s%s%s"%(num,num,num))
print(i+j+k)
"""
#Print Calendar
"""
import calendar
y = int(input("Enter the year:"))
m = int(input("Enter the month:"))
print(calendar.month(y,m))
"""
#Calculate Number of dates between two dates
"""
from datetime import *
f_date = date(2014, 7, 2)
l_date = date(2015, 7, 11)
delta = l_date  - f_date
print(delta.days)
"""
"""
from math import *
def volume(r):
    return (4/3)*pi*pow(r,3)
print("volume %.2f"%volume(1))
"""
"""
def diff(num):
    if num >= 17:
        return abs((num-17)*2)
    else:
        return num-17
print(diff(12))
print(diff(22))
"""
"""num = int(input("Enter a Number between 100 to 2000: "))
while(True):
    if num<100:
        print("Number with in 100")
        break
    elif 100<num<1000:
        print ("Number within 1000")
        break
    elif 1000<num<2000:
        print ("Number within 2000")
        break
    else:
        print("Please enter number with in range")
        break
"""
#Return the sum of three given number if the values are equal return three time of their sum1
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the second number: "))
if num1!=num2!=num3:
    print(num1+num2+num3)
else:
    ctr = 0
    while (ctr<3):
        print(num1+num2+num3)
        ctr+=1
"""
#OR
"""
def sum1(n1,n2,n3):
    if n1==n2==n3:
        return (n1+n2+n3)*3
    else:
        return n1+n2+n3
print(sum1(2,2,2))
"""
"""def strg(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
print(strg("eassy"))
"""
"""
a = input("Enter a string: ")
num = int(input("Enter the number of character you want to copy:"))
b = a[:num]
print("Original string",a)
print("Copied string:",b)
"""
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""
def str(cp,s):
    res = ""
    for i in range(cp):
        res = res + s
    return res
print(str(3,".ashu"))
"""
"""str = input("Enter String: ")
new = " "
result = ""
index = 0
for char in str:
    if (char.isalpha()):
        new+=char
new = new[::-1]
for char in str:
    if (char.isalpha()):
        result+=new[index]
        index+=1
    else:
        result+=char
print(result)
"""
"""class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def ___add__(self):
"""
"""class Computer:
    def __init__(self):
        self.name = "ashu"
        self.age = 25
    def update(self):
        self.age = 30
        self.name = "AA"
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c2 = Computer()
#c2.update()
c1.name = "pandey"
c1.age = 25
if c1.compare(c2):
    print("They are Same")
else:
    print("They are different")
print(c1.name)
print(c2.name)
"""
"""def check(num):
    if num%2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
print(check(int(input("Enter a numver"))))
"""
# without return with parameters
"""def ad(a,b):
    s = a+b
    print("sum",s)
def sa():
    ad(3,4)
    ad(5,1)

sa()
"""
# palindrome substring
"""strg = input("Enter a string: ")
count=0
for i in range(len(strg)):
    for j in range(i+1,len(strg)+1):
        temp = strg[i:j]
        if temp == temp[::-1]:
            print(temp, end = " ")
            count+=1
print("Nunber of palindrome: ",count)
"""
# OR
"""class Solution:
    def palindrome(self,s):
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    print(temp)
                    count+=1
        return count
op1 = Solution()
print(op1.palindrome("ashu"))
"""
"""a = eval(input("Enter a list: ")) # we can any datatype we want list,tuple,etc
print("a>>",a,type(a))
def test(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(test(a))"""

"""def check(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            temp = s[i:j]
            print("characters using alphabtes: ",temp)
check("aeiou")
"""
"""
import random
a = ["a","e","i","o","u"]
b = []
hh = 50
while hh>1:
    random.shuffle(a)
    d = " ".join(a)
    b.append(d)
    hh-+1
print(set(b))
"""
#WAP to print and remove every third number from a list of numbers untill it becomes Empty
"""li = [2,5,6,3,6,7,8,9]
def check(list1):
    count = 0
    while(len(list1)>0):
        if len(list1)>2:
            print(list1[2])
            list1.remove(list1[2])
        else:
            print("List is empty")
            list1.pop()
            list1.pop()
        count+=1
check(li)"""
# Unsolve QUESTION:  Find triples whose sum will be zero in a list or array
"""lis = [1,2,-3,4,6]
li = []

def trip(list):
    for i in range(len(list)):
        while((i+3)<len(list)):
            li.append(list[i:i+3])
            sum = 0
            for j in range(len(li)):
                sum = sum + li[j]
                if sum == 0:
                    return li
                else:
                    return li.clear()
x = trip(lis)
print(x)"""
# WAP to create the combinations of three digits combo..
""""numbers = []
for num in range(1):
    num = str(num).zfill(3)
print(num)
numbers.append(num)
"""
# OR
"""
import random
number = range(10)
num = random.choice(number)
combo = str(num)*3
print(combo)
"""
"""import random
def combo(num):
    d = " ".join(random.sample(num,3))
    print(d,type(d))
combo(str("ashu"))
"""
"""strg = input("Enter a string: ")
li = []
def conv(s):
    li[:0] = s
    return li
print(conv(strg))
"""
"""def A():
    print("A function")
    B()
    print("back to A")
def B():
    print("B function")
A()
"""
"""class Student():
    increament = 2
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        #self.increament = 5
    def increament(self):
        self.salary = int(self.salary * Student.increament)
        return self.salary
    @classmethod
    def change_increament(cls,amount):
        cls.increament = amount
ashu = Student("abc",26,2500)
print(ashu.salary)
Student.change_increament(2)
ashu.increament()
print(ashu.salary)"""
li = []
for i in
li.append(2)

print(li)
