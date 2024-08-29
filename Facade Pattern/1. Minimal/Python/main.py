from subsystem_class_1 import SubsystemClass1
from subsystem_class_2 import SubsystemClass2
from facade import Facade

def main():
    print("Facade Pattern in Python")
    print("------------------------")
    print()

    # Create subsystem classes.
    subsystemClass1 = SubsystemClass1()
    subsystemClass2 = SubsystemClass2()

    # Create facade.
    facade = Facade(subsystemClass1, subsystemClass2)

    # Execute facade operation.
    facade.subsystemOperation()

if __name__ == "__main__":
    main()
