class human():
    def sayhello(self,name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Helo")

obj=human()
obj.sayhello()
obj.sayhello("Parth")