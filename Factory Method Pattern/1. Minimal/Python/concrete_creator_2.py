from abstract_creator import AbstractCreator
from concrete_product_a2 import ConcreteProductA2

class ConcreteCreator2(AbstractCreator):
    def createProduct(self):
        return ConcreteProductA2()
