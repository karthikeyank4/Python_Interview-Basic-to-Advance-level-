
#_init_ keyword is mandatory

class demo:
     summation =100

     def __init__(self ,a,b):
         self.first=a
         self.second=b
         print("I am a Constructor  Method")

     # def  test(self):
     #      print("I am a normal Method")

     def data(self):
         return self.first +self.second

     def add(self):
         return self.first+self.second + demo.summation


obj=demo(2,3)
print(obj.data())
print(obj.add())

