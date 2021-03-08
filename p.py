'''
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
'''
'''
size = int(input("Enter a Number:"))
ctr = 0
for i in range(size,0,-1):#[5,4,3,2,1,0]
    for j in range(size+ctr):#[0,1,2,3,4]
        if(j>=i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    ctr = ctr+1
    print()
'''
'''
size = int(input('Enter number: '))
for i in range(size,0,-1):
    for j in range(size-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
'''
'''
size = int(input("Enter size of row:"))
ctr = 1
for i in range(65,65+size,1):
    for j in range(ctr):
        print(chr(i),end = " ")
    print()
    ctr+=1

#Convert ascii to character
'''




'''
for i in range(1,200,1):
    print("%s : %s"%(i,chr(i)))
'''
'''
ctr = 65
for i in range(5):
    for j in range(i+1):
        print(chr(chr(ctr),end=""))
        ctr = ctr+1
    print()
'''
'''
size = int(input("Enter row size:"))
for i in range(size):
    if((i+j)%2==0):
        print(1,end=" ")
    else:
        print(0,end=" ")
    print()
'''
'''
#print this symbal
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
   * * * * * * *
    * * * * *
      * * *
        *
'''
'''
size = int(input("Enter a Number:"))
ctr= 0
for i in range(size,0,-1):
    for j in range(size+ctr):
        if(j>=i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    ctr = ctr + 1
    print()
for i in range (size-1,0,-1):
    for j in range(size-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
'''
'''
* * * * *
* *     *
*   *   *
*     * *
* * * * *
'''
'''
#size = int(input("Enter a Number:"))
for i in range(size):
    for j in range(size):
        if (i==0 or )
'''
'''
import math
print(math.pi)
print(abs(-234))
print(math.ceil(4.0000))
print(math.ceil(4.1235))
print(34/5)
'''
'''
import random
#print(random.random())
print(random.randint(10,100))
print(random.randrange(10,13))
list1 = [234,345,2345,56]
print(list1)
random.shuffle(list1)
print(list1)
'''
'''
import random
start = int(input("Enter start of the range:"))
last = int(input("Enter last of the range:"))
rd = random.randint(start,last)
trial = 0
while(True):
    gn = int(input("Guess a number between  %d and %d:"%(start,last)))
    if(gn>last or gn<start):
        print("Please guess a number within range")
        continue
    elif(gn>rd):
        print("You are guessing larger Number,pls guess smaller no")
        trail = trial + 1
        last = gn
    elif(gn<rd):
        print("you are guessing smaller number,pls guess smaller no")
        trial = trial + 1
        start = gn
    elif(gn==rd):
        trial = trial + 1
        print("Congrats,You did guess no in %d trial"%trial)
        break
'''
'''
import random
print(random.randint(10,15))
'''
'''
import random
cmp = random.choice(['stone','paper','scissor'])
print("Press 1 for select stone")
print("Press 2 for select paper")
print("Press 3 for select scissor")
while(True):
    user = input("Enter your choice:")
    if(user == 1):
        u="stone"
        break
    elif(user == 2):
        u = "paper"
        break
    elif(user == 3):
        u = "scissor"
        break
    else:
        print("Please Enter valid Number:")
print("Computer choice=",cmp)
print("User choice=",u)
if((cmp =="stone" and u =="scissor") or (cmp == "paper" and u == "stone") or (cmp == "scissor" and u == "paper") ) :
    print("Computer won the match")
elif(cmp==u):
    print("Match tie")
else:
    print("User has won the Match")
'''
'''
import random
choice = input("Enter the number of Times you want to play this game:")
cmp = random.choice(['stone','paper','scissor'])
print("Press 1 for select stone")
print("Press 2 for select paper")
print("Press 3 for select scissor")
while(True):
    user = input("Enter your choice:")
    if(user == 1):
        u="stone"
        break
    elif(user == 2):
        u = "paper"
        break
    elif(user == 3):
        u = "scissor"
        break
    else:
        print("Please Enter valid Number:")
count = 0
count1 = 0
count2 = 0
for i in range(0,5,1):
    if((cmp =="stone" and u =="scissor") or (cmp == "paper" and u == "stone") or (cmp == "scissor" and u == "paper") ) :
        count1 = count1 + 1
        print("Computer won the match")
    elif(cmp==u):
        count = count + 1
    else:
        count2 = count + 1
print("Computer won time =",count1)
print("user won time =",count2)
print("Tie time=",count)
if(count1<count2):
    print("Computer won the match")
elif(count2>count1):
    print("user won the match")
elif(count1==count2):
    print("match tie")
    '''
'''
#replace
strg = "I are doing something"
print(strg)
strg.replace("are")
'''
# using while loop
'''
x = 0
while x<6:
    print("current value",x)
    x+=1
else:
    print ("loop is completed.")
'''

# add value repeatly
'''
sum1 = 0
num  = 1
print("Enter 0, to end this loop.")
while (num!=0):
    num = int(input("Enter a Number:"))
    sum1 = sum1 + num
    print ("The current sum is %d"%sum1)
else:
    print("Loop is completed")
'''
'''
from array import *
vals = array('i',[5,9,-8,5,4,34])

for e in vals:
    print(e)
'''
'''
i = 0
while (i<5):
    if i ==3:
        continue
    i+=1
    print(i)
'''
'''
x = ["1","4","2"]
x.sort()
print(x)
'''
'''
size = int(input("Enter the size of staircase:"))
for i in range(size):
    for j in range(size):
        if (j<=i):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()
'''
strg = "Ashutosh hhhh"
s = strg.count("h",2,15)
print(s)
strg = "Ashutosh asjakdhs"
print(strg.endswith("sh",0,8))
