class Father():
    def outputf(self):
       print("i am the father")

class Mother():
    def output(self):
       print("i am the mother")

class child( Father, Mother):
    def outputc(self):
       print("i am the child")

c = child()
c.outputc()
c.outputf()
c.output()