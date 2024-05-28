from concrete_factory_1 import ConcreteFactory1
from concrete_factory_2 import ConcreteFactory2

def main():
    print("Abstract Factory Pattern in Python")
    print("----------------------------------")
    print()

    createProducts(ConcreteFactory1())
    createProducts(ConcreteFactory2())

def createProducts(concreteFactory):
    productA = concreteFactory.createProductA()
    productB = concreteFactory.createProductB()

    productA.build()
    productB.build()

if __name__ == "__main__":
    main()
