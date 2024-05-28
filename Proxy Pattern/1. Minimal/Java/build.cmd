@echo off

javac *.java
jar cvfm ProxyDemo.jar Manifest.txt *.class
