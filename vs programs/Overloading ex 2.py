class example:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a + b.a

sum_1=example(int(input(print("Enter your value A :"))))
sum_2=example(int(input(print("Enter your value B :"))))
print(sum_1 + sum_2)
mrg_1=example(str(input(print("Enter your value A :"))))
mrg_2=example(str(input(print("Enter your value B :"))))
print(mrg_1 + mrg_2)