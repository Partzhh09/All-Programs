class car():
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def dispay(self):
        print(self.name)
        print(self.price)

class tata(car):
    def __init__(self,name,price,model):
        self.model = model

        car.__init__(self,name,price)

class hyundai(car):
    def __init__(self,name,price,colour):
        self.colour = colour

        car.__init__(self,name,price)

class ford(car):
    def __init__(self,name,price,speed):
        self.speed = speed

        car.__init__(self,name,price)

car_1=car("Fortuner","32.59 lakh")
car_1.dispay()
car_2=car("I20","11.62 lakh")
car_2.dispay()
car_3=car("Endeavour","36.25 lakh")
car_3.dispay()