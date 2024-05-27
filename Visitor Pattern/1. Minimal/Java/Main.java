public class Main {
    public static void main(String[] args) {
        System.out.println("Visitor Pattern in Java");
        System.out.println("-----------------------");
        System.out.println();
        
        Element elementA = new ConcreteElementA();
        Element elementB = new ConcreteElementB();
    
        Visitor visitorA = new ConcreteVisitorA();
        Visitor visitorB = new ConcreteVisitorB();
    
        elementA.accept(visitorA);
        elementA.accept(visitorB);
    
        elementB.accept(visitorA);
        elementB.accept(visitorB);
    }
}
