from abstract_subject import AbstractSubject
from real_subject import RealSubject

class ProxySubject(AbstractSubject):
    def __init__(self):
        self.real_subject = None

    def doSomething(self):
        if self.real_subject is None:
            self.real_subject = RealSubject()

        self.real_subject.doSomething()
