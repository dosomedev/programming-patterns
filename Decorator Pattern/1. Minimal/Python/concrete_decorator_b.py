from abstract_decorator import AbstractDecorator

class ConcreteDecoratorB(AbstractDecorator):
    def operation(self):
        super().operation()
        self.added_behavior()
    
    def added_behavior(self):
        print("Added behavior from ConcreteDecoratorB.")
