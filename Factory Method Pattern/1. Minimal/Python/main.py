from concrete_creator_1 import ConcreteCreator1
from concrete_creator_2 import ConcreteCreator2

def main():
    print("Factory Method Pattern in Python")
    print("--------------------------------")
    print()

    creator1 = ConcreteCreator1()
    creator2 = ConcreteCreator2()

    productA1 = creator1.createProduct()
    productA2 = creator2.createProduct()

    productA1.doSomething()
    productA2.doSomething()

if __name__ == "__main__":
    main()
