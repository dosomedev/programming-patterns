from adaptee import Adaptee
from target import Target

class ClassAdapter(Adaptee, Target):
    def request(self):
        self.specificRequest()
