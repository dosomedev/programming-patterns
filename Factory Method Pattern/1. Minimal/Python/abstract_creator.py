from abc import ABC, abstractmethod

class AbstractCreator(ABC):
    @abstractmethod
    def createProduct(self):
        pass
