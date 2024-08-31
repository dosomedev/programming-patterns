package com.dosomedev;

import java.util.HashMap;
import java.util.Map;

public class ShapeFactory {
    private static final Map<String, Shape> prototypes = new HashMap<>();

    static {
        prototypes.put("circle", new Circle(40));
        prototypes.put("square", new Square(120));
        prototypes.put("rectangle", new Rectangle(210, 140));
    }
    
    public static Shape createShape(String type) {
        Shape prototype = prototypes.get(type);
        if (prototype == null) {
            throw new IllegalArgumentException("Unknown shape type "
                + type + ".");
        }

        return prototype.clone();
    }
}
