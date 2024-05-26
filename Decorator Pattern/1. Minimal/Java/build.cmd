@echo off

javac *.java
jar cvfm DecoratorDemo.jar Manifest.txt *.class
