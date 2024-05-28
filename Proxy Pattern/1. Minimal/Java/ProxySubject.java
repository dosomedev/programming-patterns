public class ProxySubject implements AbstractSubject {
    private RealSubject realSubject;

    @Override
    public void doSomething() {
        if (this.realSubject == null) {
            this.realSubject = new RealSubject();
        }

        this.realSubject.doSomething();
    }
}
