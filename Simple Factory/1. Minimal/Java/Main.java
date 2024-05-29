public class Main {
    public static void main(String[] args) {
        System.out.println("Simple Factory in Java");
        System.out.println("----------------------");
        System.out.println();

        Product product1 = ProductFactory.createProduct("Product1");
        Product product2 = ProductFactory.createProduct("Product2");

        product1.operation();
        product2.operation();
    }
}
