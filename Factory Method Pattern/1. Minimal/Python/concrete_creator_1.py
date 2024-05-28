from abstract_creator import AbstractCreator
from concrete_product_a1 import ConcreteProductA1

class ConcreteCreator1(AbstractCreator):
    def createProduct(self):
        return ConcreteProductA1()
