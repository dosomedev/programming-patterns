public class ConcretePrototype2 implements Prototype {
    private String value;

    public ConcretePrototype2(String value) {
        this.value = value;
    }

    @Override
    public Prototype clone() {
        return new ConcretePrototype2(this.value);
    }

    @Override
    public String toString() {
        return "value = '" + this.value + "'";
    }
}
