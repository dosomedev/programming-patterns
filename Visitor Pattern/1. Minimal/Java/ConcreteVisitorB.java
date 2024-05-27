public class ConcreteVisitorB implements Visitor {
    @Override
    public void visit(ConcreteElementA element) {
        System.out.println("ConcreteVisitorB visits ConcreteElementA: " + element.operationA());
    }
  
    @Override
    public void visit(ConcreteElementB element) {
        System.out.println("ConcreteVisitorB visits ConcreteElementB: " + element.operationB());
    }
}
