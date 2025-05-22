class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " , self.name)
        print("My age is" , self.age)

p1=person("Parth",17)
p1.myfunc()