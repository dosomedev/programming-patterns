from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def build(self):
        pass
