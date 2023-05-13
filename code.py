# Closure
# before understanding python closure, we must understand what is 
# nested function and what is non-local variable
# nested function is a function that is nested inside another function
# non-local variable is a variable that is neither local nor global
# it is a variable that is defined inside a nested function and is used
# inside the nested function
# example:
def outer_function(x):
    def inner_function(y):
        nonlocal x
        x += y
        return x
    return inner_function

add5 = outer_function(5)
print(add5(2)) # output : 7
print(add5(3)) # output : 10

# in the above example, the inner_function is a nested function and x is a 
# non-local variable, and if we talk about the closure, we have another example

def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(2)) # output : 7
print(add10(2)) # output : 12

# here, make_adder returns a closure that create new 'adder' function
# that ads the value of 'x' (which is retained from the enclosing scope)
# to the argument passed to the 'adder' function

# uses of Python closure: Encapsulation, function factories, callback
# functions, decorators, etc.


# Decorators
# Decorators are very powerful and useful tool in Python since it allows
# programmers to modify the behavior of function or class. Decorators allow
# us to wrap another function in order to extend the behavior of wrapped 
# function, without permanently modifying it.

# examples:
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print('I am ordinary')
ordinary()
# Decorators in Python
# Decorators can also be useful to attach data (or add attribute) to functions
# in Python. This is similar to defining static variable in a function.
# example:
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

result = divide(10, 0)
print(result)