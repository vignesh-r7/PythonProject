class Father():
    def outputf(self):
       print("i am the father")

class Child1(Father):
    def output(self):
       print("i am the child1")

class child2(Father):
    def outputc(self):
       print("i am the child2")

c=Child1()
c2=child2()
c.output()
c.outputf()
c2.outputc()
c2.outputf()


