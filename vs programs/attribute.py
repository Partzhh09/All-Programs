class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displaycount(self):
        print("Total Employee%d" % Employee.empcount)

    def displayEmployee(self):
        print("Name :",self.name ,"salary :",self.salary)

emp1=Employee("Parth",5000)
emp2=Employee("Dhrvu",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empcount)