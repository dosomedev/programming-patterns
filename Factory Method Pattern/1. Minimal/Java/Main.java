public class Main {
    public static void main(String[] args) {
        System.out.println("Factory Method Pattern in Java");
        System.out.println("------------------------------");
        System.out.println();
  
        AbstractCreator creator1 = new ConcreteCreator1();
        AbstractCreator creator2 = new ConcreteCreator2();

        AbstractProduct productA1 = creator1.createProduct();
        AbstractProduct productA2 = creator2.createProduct();

        productA1.doSomething();
        productA2.doSomething();
    }
}
