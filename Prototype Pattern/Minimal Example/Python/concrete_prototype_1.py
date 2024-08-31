from prototype import Prototype

class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        return ConcretePrototype1(self._value)
    
    def __str__(self):
        return "value = '" + self._value + "'"
