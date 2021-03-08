"""def outer():
    x= 3
    print(x)
    def inner():
        y = 7
        return x+y
    return inner
a = outer()
print(a.__name__)
"""
# Decorator
"""def outer(func):
    def inner(Name):
        if Name == "Sam":
            return "Good Marning Sam"
        return Name
    return inner
@outer
def email(name):
    return "hello" + " " +  name
print(email("Sam"))
print(email("Ashu"))
"""
#example
"""def outer(func):            # taking print_out function as parameter
    def inner():               # Add functionality to inner func
        str1 = func()          # calling print_out function and storing to a variable called str1
        return str1.upper()    # return str1 value to inner function
    return inner               # return inner function values to outer function we can also call inner function like inner() byt then we have to use print_out instead of print_out()
@outer                         # connect decorator
def print_out():
    return "gooD morning"
print(print_out())            # calling and printing function using decorator
"""
