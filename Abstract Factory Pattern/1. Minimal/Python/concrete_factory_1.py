from abstract_factory import AbstractFactory
from concrete_product_a1 import ConcreteProductA1
from concrete_product_b1 import ConcreteProductB1

class ConcreteFactory1(AbstractFactory):
    def createProductA(self):
        return ConcreteProductA1()
    
    def createProductB(self):
        return ConcreteProductB1()
