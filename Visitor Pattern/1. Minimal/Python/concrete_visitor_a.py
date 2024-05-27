from visitor import Visitor

class ConcreteVisitorA(Visitor):
    def visit_concrete_element_a(self, element_a):
        print("ConcreteVisitorA visits ConcreteElementA:", element_a.operation_a())

    def visit_concrete_element_b(self, element_b):
        print("ConcreteVisitorA visits ConcreteElementB:", element_b.operation_b())
