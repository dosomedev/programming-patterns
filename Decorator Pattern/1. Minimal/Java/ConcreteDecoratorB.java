public class ConcreteDecoratorB extends AbstractDecorator {
    public ConcreteDecoratorB(AbstractComponent component) {
        super(component);
    }

    @Override
    public void operation() {
        super.operation();
        this.addedBehavior();
    }

    private void addedBehavior() {
        System.out.println("Added behavior from ConcreteDecoratorB.");
    }
}
