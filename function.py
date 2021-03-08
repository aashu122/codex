'''
def say_hi():
    print("Mike")
print("Top")
say_hi() #call the function This will print the value which is passed inside the function
print("Bottom")
'''
'''
def say_hi(name,age):
    print("Hello " +name+ ", you are "+age)# +sign concanate the value

say_hi("Mike","35")
say_hi("Steve", "70")
'''
'''
strg = "python"
print(strg)
print(type(strg))
strg = '"Rams Father"'
print(strg)
strg = """first line
second line
third line"""
print(strg)
strg = '''"Ram's Father"'''
print(strg)
strg1 = "hello"
strg2 = "python"
print(strg1+" "+strg2)
strg = "hello man how are you"
print("man" in strg)
print(strg)
print(len(strg))
print(strg[:])
print(strg[0:5:1])
print(strg[len(strg)::-1])
'''
'''
strg = input("Enter string:")
print(strg.lower())
print(strg.upper())
print(strg.capitalize())
print(strg.title())
'''
'''
strg = input("Enter string: ")
print(strg.islower())
print(strg.isupper())
'''
'''
strg = "hello my name is Ashutosh"
c = 0
for i in strg:
    if(i == "o"):
        c+=1
print(c)
'''
'''
n = int(input("Enter a Number:"))
if(n%2!=0 ):
    print("Weird")

elif(n%2==0):
    if(2<=n<=5):
        print("Not Weird")
    elif(6<=n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")
'''
'''
size = int(input("Enter a Number:" ))
for i in range(5):
        print(i, end ="")
'''
'''
def cube(num):
    return num*num*num
result = cube(3)
print(result)
'''
'''
guess = input("Enter guess word:")
secret_word = "apple"
guess_limit = 3
guess_count = 0
while(guess!=secret_word):
    if(guess_limit>guess_count):

        guess_count +=1
    else:
        print("Out of guess, YOU LOOSE!")
if(guess == secret_word):
    print("You Win")
'''
'''
def std(name,clas,**marks): # *symbal using multiple keywords
    # ** using multiple keywords
    #star define the all value will be printed inside the marks parameters
    print("Name: ",name)
    print("Clas:",clas)
    #print("Marks:",marks)
    for x,y in marks.items():
        print(x + " Marks :",y)
std("Ashu",10,English = 80,Math = 70,History = 80)
'''
