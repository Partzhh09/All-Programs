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

obj=college("Parth",9517536482,2022,"CSE")
obj.display()