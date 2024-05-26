abstract class AbstractDecorator implements AbstractComponent {
    protected AbstractComponent component;

    public AbstractDecorator(AbstractComponent component) {
        this.component = component;
    }

    @Override
    public void operation() {
        this.component.operation();
    }
}
