from abc import ABC, abstractmethod

class AbstractSubject(ABC):
    @abstractmethod
    def doSomething(self):
        pass
