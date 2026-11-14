class encap():
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class encap1(encap):
    def output(self):
        print(self._b)
        print(self.__a)
c = encap1(4,5)
c.output()