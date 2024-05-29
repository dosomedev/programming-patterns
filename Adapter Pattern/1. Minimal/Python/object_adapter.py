from target import Target

class ObjectAdapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def request(self):
        self.adaptee.specificRequest()
