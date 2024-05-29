@echo off

javac *.java
jar cvfm PrototypeDemo.jar Manifest.txt *.class
