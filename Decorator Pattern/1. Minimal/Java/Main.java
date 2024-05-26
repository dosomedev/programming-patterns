public class Main {
    public static void main(String[] args) {
        System.out.println("Decorator Pattern in Java");
        System.out.println("-------------------------");
        System.out.println();
        
        // Creating a concrete component.
        AbstractComponent component = new ConcreteComponent();
        System.out.println("Concrete Component:");
        component.operation();

        System.out.println();

        // Decorating the concrete component with the concrete decorator a.
        AbstractComponent decoratedCompontentA = new ConcreteDecoraterA(component);
        System.out.println("Decorated Component A:");
        decoratedCompontentA.operation();

        System.out.println();

        // Decorating the concrete component with the concrete decorator b.
        AbstractComponent decoratedComponentB = new ConcreteDecoratorB(component);
        System.out.println("Decorated Component B:");
        decoratedComponentB.operation();

        System.out.println();

        // Decorating the concrete component with both concrete decorators nested.
        AbstractComponent decoratedComponentAB = new ConcreteDecoratorB(new ConcreteDecoraterA(component));
        System.out.println("Decorated Component AB:");
        decoratedComponentAB.operation();
    }
}
