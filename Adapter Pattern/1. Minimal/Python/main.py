from class_adapter import ClassAdapter
from object_adapter import ObjectAdapter
from adaptee import Adaptee

def main():
    print("Adapter Pattern in Python")
    print("-------------------------")
    print()
    
    # Using class adapter.
    classAdapter = ClassAdapter()
    classAdapter.request()

    # Using object adapter.
    adaptee = Adaptee()
    objectAdapter = ObjectAdapter(adaptee)
    objectAdapter.request()

if __name__ == "__main__":
    main()
