@echo off

javac *.java
jar cvfm SingletonDemo.jar Manifest.txt *.class
