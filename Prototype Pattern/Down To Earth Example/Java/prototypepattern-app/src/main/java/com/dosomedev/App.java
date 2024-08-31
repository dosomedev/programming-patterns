package com.dosomedev;

/**
 * Down To Earth Prototype Pattern Example.
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Shape circle = ShapeFactory.createShape("circle");
        circle.draw();

        Shape square = ShapeFactory.createShape("square");
        square.draw();

        Shape rectangle = ShapeFactory.createShape("rectangle");
        rectangle.draw();
    }
}
