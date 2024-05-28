public class ConcreteCreator1 implements AbstractCreator {
    @Override
    public AbstractProduct createProduct() {
        return new ConcreteProductA1();
    }
}
