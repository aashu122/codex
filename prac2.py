"""strg = "hello my name is ashu"
def ctr(s):
    d = {}
    for i in s:
        if i in s:
            d[i] = d[i] + 1
        else:
             d[i] = 1
    print("All character is strg" + str(d))
print(ctr(strg))

"""
# install modules
"""from sys import modules

for num, module_name in enumerate(modules):
    print(f"{num}-- {module_name}")
"""
"""import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)"""
# Print all three possible combination which give 70 at there addition
'''import numpy
arr1 = numpy.array([10,20,20,20])
arr2 = numpy.array([10,20,30,40])
arr3 = numpy.array([10,30,40,20])
def add(array):
    for i in array:
        for j in array:
            for k in array:
                if i+j+k == 70:
                    sum = i+j+k
                    print(" {} + {} + {} = {}".format(i,j,k,sum))
                else:
                    continue

add(arr1)
print(" Second Array")
add(arr2)
print("Third array")
add(arr3)
'''
# count the frequency in a string of character
"""def con(S):
    c = {}
    for i in S:
        c[i] = int(S.count(i))
    print(c)
strg = "google.com"
con(strg)
"""
#OR
"""def char_fre(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_fre("google.com"))
"""
# input: ashutosh output: assh if string has two char return asas

"""def rechar(S):
    if len(S)<2:
        return EmptyString
    elif len(S) == 2:
        return S+S
    elif len(S)>2:
        return S[0:2] + S[-2::1]
print(rechar("as"))"""
"""def name(data):
    print("Name>>",data)
    def age(data1):
        print("data1>>",data1)
    return age
# print("calling function",name("Ashutosh"))
s = name("Ashutosh")"""
"""import numpy
def fetch(arr):
    li = numpy.array(arr,int)
    li.shape= (3,3)
    return li
a1 = input().strip().split(" ")
result = fetch(a1)
print(result)"""
# Transpose and flatten inbuild method
"""import numpy
def f():
    n, m = map(int, input().split())
    arr = numpy.array([input().strip().split() for _ in range(n)], int)
    return arr
c = f()
print (c.transpose())
print (c.flatten())"""
"""R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
mat = [[int(input()) for x in range (C)] for y in range(R)]
print(mat)"""
#change string value except first value
# string object does not support item assignment
"""strg = input("Enter a string: ")
s = strg[0]
for i in range(1,len(strg)):
    if strg[i] == s:
        strg = strg.replace(s,"$")
        strg = s + strg[1:]
print(strg)"""
# I/P  return O/P retu$n
