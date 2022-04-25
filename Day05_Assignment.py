# Assignment 1

def nozero(fnc):
    def helper(*args):
        print("logged in to service")
        print(fnc(*args))
        print("logged out of the service")
        print("-"*40)
    return helper

@nozero
def div(x, y):
    print("division function called")
    return x/y

@nozero
def mul(x, y):
    print("multiple function called..")
    return x*y

@nozero
def add(x,y):
    print("add function called...")
    return x+y

@nozero
def sub(x, y):
    print("sub function called..")
    return x-y

div(13, 15)
mul(24, 56)
add(56,87)
sub(65,54)

# assignment 3

def logBeforeAfter(fnc):
    def helper(*args):
        print("logged in before")
        fnc(*args)
        print("logged out after")
        print("-" * 40)
    return helper


@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args)

@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
    print("fun3", args, kwargs)


fun(2,3)
fun1(4,fun)
fun2()
fun3(fun1,fun2)




