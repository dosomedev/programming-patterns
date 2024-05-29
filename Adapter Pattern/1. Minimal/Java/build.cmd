@echo off

javac *.java
jar cvfm AdapterDemo.jar Manifest.txt *.class
