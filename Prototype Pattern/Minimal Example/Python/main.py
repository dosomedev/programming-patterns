from concrete_prototype_1 import ConcretePrototype1
from concrete_prototype_2 import ConcretePrototype2

def main():
    print("Prototype Pattern in Python")
    print("---------------------------")
    print()

    # Create concrete prototypes.
    cp1 = ConcretePrototype1("cp1")
    cp2 = ConcretePrototype2("cp2")

    # Clone concrete prototypes.
    cp3 = cp1.clone()
    cp4 = cp2.clone()

    # Compare concrete prototypes.
    print("cp1:", cp1, ", hash =", hash(cp1))
    print("cp2:", cp2, ", hash =", hash(cp2))
    print("cp3:", cp3, ", hash =", hash(cp3))
    print("cp4:", cp4, ", hash =", hash(cp4))
    
if __name__ == "__main__":
    main()
