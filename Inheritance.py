class Food:
    def __init__(self,name, price):
        self.name=name
        self.price=price
        print(f"{self.name} Is Created From Base Class")
    def eat(self):
        print("eat method from base class")

class Apple(Food):
    def __init__(self,name,price,amount):
        super().__init__(name,price)
        self.amount=amount
        print(f"{self.name} is created from derived class and price is {self.price} and amount is {self.amount}")
    def get_from_tree(self):
        print("get from tree from derived class")
food_two = Apple("Pizza",150,500)
food_two.eat()
