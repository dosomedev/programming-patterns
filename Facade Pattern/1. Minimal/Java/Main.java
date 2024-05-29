public class Main {
    public static void main(String[] args) {
        System.out.println("Facade Pattern in Java");
        System.out.println("----------------------");
        System.out.println();
        
        // Create subsystem classes.
        SubsystemClass1 subsystemClass1 = new SubsystemClass1();
        SubsystemClass2 subsystemClass2 = new SubsystemClass2();

        // Create facade.
        Facade facade = new Facade(subsystemClass1, subsystemClass2);

        // Execute facade operation.
        facade.subsystemOperation();
    }
}
