class student():
    def __init__(self,name,enrollnumber):
        self.name = name
        self.enrollnumber = enrollnumber
    
    def display(self):
        print(self.name)
        print(self.enrollnumber)

class college(student):
    def __init__(self,name,enrollnumber,admnyear,branch):
        self.admnyear = admnyear
        self.branch = branch

        student.__init__(self,name,enrollnumber)

class university(student):
    def __init__(self,name,enrollnumber,refno,branch):
        self.refno = refno
        self.branch = branch

        student.__init__(self,name,enrollnumber)

obj_1=college("Parth",9517536482,2022,"CSE")
obj_1.display()
obj_2=university("Parth",9517536482,2022,"CSE")
obj_2.display()