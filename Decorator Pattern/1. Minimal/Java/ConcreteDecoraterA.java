public class ConcreteDecoraterA extends AbstractDecorator {
    public ConcreteDecoraterA(AbstractComponent component) {
        super(component);
    }

    @Override
    public void operation() {
        super.operation();
        this.addedBehavior();
    }

    private void addedBehavior() {
        System.out.println("Added behavior from ConcreteDecoratorA.");
    }
}
