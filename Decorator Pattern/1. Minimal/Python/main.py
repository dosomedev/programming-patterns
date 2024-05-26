from concrete_component import ConcreteComponent
from concrete_decorator_a import ConcreteDecoratorA
from concrete_decorator_b import ConcreteDecoratorB

def main():
    print("Decorator Pattern in Python")
    print("---------------------------")
    print()
    
    # Creating a concrete component.
    component = ConcreteComponent()
    print("Concrete Component:")
    component.operation()

    print()

    # Decorating the concrete component with the concrete decorator a.
    decorated_component_a = ConcreteDecoratorA(component)
    print("Decorated Component A:")
    decorated_component_a.operation()

    print()

    # Decorating the concrete component with the concrete decorator b.
    decorated_component_b = ConcreteDecoratorB(component)
    print("Decorated Component B:")
    decorated_component_b.operation()

    print()

    # Decorating the concrete component with both concrete decorators nested.
    decorated_component_ab = ConcreteDecoratorB(ConcreteDecoratorA(component))
    print("Decorated Component AB:")
    decorated_component_ab.operation()

if __name__ == "__main__":
    main()
