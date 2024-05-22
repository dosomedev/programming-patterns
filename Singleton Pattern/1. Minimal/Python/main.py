from singleton import Singleton

def main():
    print("Singleton Pattern in Python")
    print("---------------------------")
    print()

    s1 = Singleton()
    s2 = Singleton()

    print("Same instance in s1 and s2: ", end="")
    print(s1 is s2)

    print(s1._instance)
    print(s2._instance)

    s1.setMessage("Hello s1!")

    s1.showMessage()
    s2.showMessage()

    s2.setMessage("Hello s2!")

    s1.showMessage()
    s2.showMessage()

if __name__ == "__main__":
    main()
