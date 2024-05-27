public class ConcreteVisitorA implements Visitor {
    @Override
    public void visit(ConcreteElementA element) {
        System.out.println("ConcreteVisitorA visits ConcreteElementA: " + element.operationA());
    }
  
    @Override
    public void visit(ConcreteElementB element) {
        System.out.println("ConcreteVisitorA visits ConcreteElementB: " + element.operationB());
    }
}
