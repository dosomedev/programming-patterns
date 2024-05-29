@echo off

javac *.java
jar cvfm FacadeDemo.jar Manifest.txt *.class
