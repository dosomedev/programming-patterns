from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def createProductA(self):
        pass

    @abstractmethod
    def createProductB(self):
        pass
