class parent():
    def output(self):
       print("i am the parent")

class child(parent):
    def outputc(self):
       print("i am the child")

c = child()
c.outputc()
c.output()



class grandparent():
    def outputgf(self):
       print("i am the grandparent")

class parent(grandparent):
    def output(self):
       print("i am the parent")

class child(parent):
    def outputc(self):
       print("i am the child")

c = child()
c.outputc()
c.output()
c.outputgf()