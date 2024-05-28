public class Main {
    public static void main(String[] args) {
        System.out.println("Proxy Pattern in Java");
        System.out.println("---------------------");
        System.out.println();

        System.out.println("Create proxy instance.");
        AbstractSubject subject = new ProxySubject();

        System.out.println("Call proxy doSomething method.");
        subject.doSomething();
        System.out.println("Call proxy doSomething method again.");
        subject.doSomething();
    }
}
