@echo off

javac *.java
jar cvfm SimpleFactoryDemo.jar Manifest.txt *.class
