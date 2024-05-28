from abstract_factory import AbstractFactory
from concrete_product_a2 import ConcreteProductA2
from concrete_product_b2 import ConcreteProductB2

class ConcreteFactory2(AbstractFactory):
    def createProductA(self):
        return ConcreteProductA2()
    
    def createProductB(self):
        return ConcreteProductB2()
