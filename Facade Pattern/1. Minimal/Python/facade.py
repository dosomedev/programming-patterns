class Facade:
    def __init__(self, subsystemClass1, subsystemClass2):
        self._subsystemClass1 = subsystemClass1
        self._subsystemClass2 = subsystemClass2

    def subsystemOperation(self):
        self._subsystemClass1.operationOne()
        self._subsystemClass2.operationTwo()
