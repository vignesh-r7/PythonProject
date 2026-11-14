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
    print(a+b)
add(4,5)  




def make_coffee():
    print("lit up stove")
    print("make coffee")
    print("add milk")
    print("drink coffee")

print("wake up")
make_coffee()
print("work for a while")
make_coffee()



def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)

