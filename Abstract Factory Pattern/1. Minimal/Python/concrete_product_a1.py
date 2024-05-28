from abstract_product_a import AbstractProductA

class ConcreteProductA1(AbstractProductA):
    def build(self):
        print("Building concrete product A1")
