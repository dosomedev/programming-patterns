from visitor import Visitor

class ConcreteVisitorB(Visitor):
    def visit_concrete_element_a(self, element_a):
        print("ConcreteVisitorB visits ConcreteElementA:", element_a.operation_a())

    def visit_concrete_element_b(self, element_b):
        print("ConcreteVisitorB visits ConcreteElementB:", element_b.operation_b())
