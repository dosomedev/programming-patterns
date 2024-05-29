from product_factory import ProductFactory

def main():
    print("Simple Factory in Python")
    print("------------------------")
    print()

    product1 = ProductFactory.createProduct("Product1")
    product2 = ProductFactory.createProduct("Product2")

    product1.operation()
    product2.operation()

if __name__ == "__main__":
    main()
