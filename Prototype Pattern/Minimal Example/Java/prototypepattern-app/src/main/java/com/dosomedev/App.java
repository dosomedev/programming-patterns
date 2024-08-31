package com.dosomedev;

/**
 * Prototype Pattern Example.
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println("Prototype Pattern in Java");
        System.out.println("-------------------------");
        System.out.println();

        // Create concrete prototypes.
        Prototype cp1 = new ConcretePrototype1("cp1");
        Prototype cp2 = new ConcretePrototype2("cp2");

        // Clone concrete prototypes.
        Prototype cp3 = cp1.clone();
        Prototype cp4 = cp2.clone();

        // Compare concrete prototypes.
        System.out.println("cp1: " + cp1 + ", hash = " + cp1.hashCode());
        System.out.println("cp2: " + cp2 + ", hash = " + cp2.hashCode());
        System.out.println("cp3: " + cp3 + ", hash = " + cp3.hashCode());
        System.out.println("cp4: " + cp4 + ", hash = " + cp4.hashCode());
    }
}
