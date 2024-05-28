from abstract_product_b import AbstractProductB

class ConcreteProductB1(AbstractProductB):
    def build(self):
        print("Building concrete product B1")
