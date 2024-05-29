public class Main {
    public static void main(String[] args) {
        System.out.println("Adapter Pattern in Java");
        System.out.println("-----------------------");
        System.out.println();
        
        // Using class adapter.
        Target classAdapter = new ClassAdapter();
        classAdapter.request();

        // Using object adapter.
        Adaptee adaptee = new Adaptee();
        Target objectAdapter = new ObjectAdapter(adaptee);
        objectAdapter.request();
    }
}
