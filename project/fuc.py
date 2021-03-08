'''
class Area():
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def __eq__(self,another):
        if isinstance(antother,Area):
            return self.height * self.width == another.height * another.width
        else:
            return False
a1 = Area(7,10)
a2 = Area(35,2)
a3 = Area(8,9)
print("Testing ==")
print(a1=="hello")
print(a1==a2)
print(a1==a3)
print(a2==a3)
'''
# WAF of factorial number!
'''
def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be psitive and integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(0))
'''
# Find sum of
'''
d2 = {"a":152,"b":78,"c":78+3j,1:"sdfdg",2.3:"SDfdsf",
              "lst":[12,132,"sdf",165,4,6,46,46,6,64],
              "tup":(12,46,4,9,49,9,"SF"),
              "st":{1,1,2,3,5,6,6,9,9},
                "d":{"a":152,"b":78,"c":78+3j},
              "lst":[12,132,"sdf",165,4,6,46,46,6,64],
              "tup":(12,46,4,9,49,9,"SF"),
              "st":{1,1,2,3,5,6,6,9,9}}
count = 0
for elements in d2:
    print(elements)
    count+=1

print("Number of elements in",count)
print(len(d2))
'''
'''
T = int(input("Enter number: ").strip())

L = []
for t in range(T):
    args = input("Enter a append for add,").strip().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print (L)
        '''
