from abstract_product_a import AbstractProductA

class ConcreteProductA2(AbstractProductA):
    def build(self):
        print("Building concrete product A2")
