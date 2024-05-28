public class RealSubject implements AbstractSubject {
    public RealSubject() {
        System.out.println("Create real instance.");
    }

    @Override
    public void doSomething() {
        System.out.println("Execute real doSomething method.");
    }
}
