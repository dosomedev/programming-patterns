public class Main {
    public static void main(String[] args) {
        System.out.println("Abstract Factory Pattern in Java");
        System.out.println("--------------------------------");
        System.out.println();
  
        createProducts(new ConcreteFactory1());
        createProducts(new ConcreteFactory2());
    }

    private static void createProducts(AbstractFactory concreteFactory) {
        AbstractProductA productA = concreteFactory.createProductA();
        AbstractProductB productB = concreteFactory.createProductB();

        productA.build();
        productB.build();
    }
}
