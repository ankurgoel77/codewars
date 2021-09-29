#https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def plus(x):
    return lambda y: x+y
def minus(x):
    return lambda y : y-x
def times(x):
    return lambda y : y*x
def divided_by(x):
    return lambda y : y // x

def zero(f=plus(0)):
    return f(0)
def one(f=plus(0)):
    return f(1)
def two(f=plus(0)):
    return f(2)
def three(f=plus(0)):
    return f(3)
def four(f=plus(0)):
    return f(4)
def five(f=plus(0)):
    return f(5)
def six(f=plus(0)):
    return f(6)
def seven(f=plus(0)):
    return f(7)
def eight(f=plus(0)):
    return f(8)
def nine(f=plus(0)):
    return f(9)


