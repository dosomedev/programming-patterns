from abstract_subject import AbstractSubject

class RealSubject(AbstractSubject):
    def __init__(self):
        print("Create real instance.")

    def doSomething(self):
        print("Execute real doSomething method.")
