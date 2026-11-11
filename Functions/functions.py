def fun():
    print("this is function")
fun()


def fun(a,b,c):
    print("this is function",a,b,c)
fun(4,5,6)


def fun(*a):
    print("this is function",a)
fun(4,5,6)



def fun(**a):
    print("this is function",a)
fun(a=77,b=99,c="dd")



def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()



def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)

