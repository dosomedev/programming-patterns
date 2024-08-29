from target import Target
from adaptee import Adaptee

class ObjectAdapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    
    def request(self):
        self.adaptee.specificRequest()
