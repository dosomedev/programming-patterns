@echo off

javac *.java
jar cvfm VisitorDemo.jar Manifest.txt *.class
