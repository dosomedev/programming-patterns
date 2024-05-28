@echo off

javac *.java
jar cvfm AbstractFactoryDemo.jar Manifest.txt *.class
