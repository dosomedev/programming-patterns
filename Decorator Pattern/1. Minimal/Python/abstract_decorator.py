from abstract_component import AbstractComponent

class AbstractDecorator(AbstractComponent):
    def __init__(self, component):
        self._component = component

    def operation(self):
        self._component.operation()
