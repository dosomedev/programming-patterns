package com.dosomedev;

public class Square implements Shape {
    private int sideLength;

    public Square(int sideLength) {
        this.sideLength = sideLength;
    }

    @Override
    public Shape clone() {
        return new Square(this.sideLength);
    }

    @Override
    public void draw() {
        System.out.println("Drawing of a square with the side length "
            + this.sideLength + ".");
    }
}
