from concrete_element_a import ConcreteElementA
from concrete_element_b import ConcreteElementB
from concrete_visitor_a import ConcreteVisitorA
from concrete_visitor_b import ConcreteVisitorB

def main():
    print("Visitor Pattern in Python")
    print("-------------------------")
    print()
    
    elementA = ConcreteElementA()
    elementB = ConcreteElementB()

    visitorA = ConcreteVisitorA()
    visitorB = ConcreteVisitorB()

    elementA.accept(visitorA)
    elementA.accept(visitorB)

    elementB.accept(visitorA)
    elementB.accept(visitorB)

if __name__ == "__main__":
    main()
