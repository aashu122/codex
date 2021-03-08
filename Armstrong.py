num1 = int(input("Enter a number:"))
sum = 0
num = num1
while(num>0):
    r = num%10
    sum = sum + r**3
    num = num//10
if (num1 == sum):
    print(num1,"is a armstrong number")
else:
    print(num1,"is not a armstrong Number")
