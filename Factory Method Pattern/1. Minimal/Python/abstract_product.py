from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def doSomething(self):
        pass
