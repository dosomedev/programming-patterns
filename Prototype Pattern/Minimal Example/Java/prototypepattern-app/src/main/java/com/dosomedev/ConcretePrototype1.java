package com.dosomedev;

public class ConcretePrototype1 implements Prototype {
    private String value;

    public ConcretePrototype1(String value) {
        this.value = value;
    }

    @Override
    public Prototype clone() {
        return new ConcretePrototype1(this.value);
    }

    @Override
    public String toString() {
        return "value = '" + this.value + "'";
    }
}
