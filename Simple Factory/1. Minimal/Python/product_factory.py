from product_1 import Product1
from product_2 import Product2

class ProductFactory:
    @staticmethod
    def createProduct(productType):
        if productType == "Product1":
            return Product1()
        elif productType == "Product2":
            return Product2()
        return None
