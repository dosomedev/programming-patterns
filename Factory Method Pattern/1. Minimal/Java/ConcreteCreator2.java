public class ConcreteCreator2 implements AbstractCreator {
    @Override
    public AbstractProduct createProduct() {
        return new ConcreteProductA2();
    }
}
