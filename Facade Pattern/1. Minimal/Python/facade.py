from subsystem_class_1 import SubsystemClass1
from subsystem_class_2 import SubsystemClass2

class Facade:
    def __init__(
            self,
            subsystemClass1: SubsystemClass1,
            subsystemClass2: SubsystemClass2
        ):
        self._subsystemClass1 = subsystemClass1
        self._subsystemClass2 = subsystemClass2

    def subsystemOperation(self):
        self._subsystemClass1.operationOne()
        self._subsystemClass2.operationTwo()
