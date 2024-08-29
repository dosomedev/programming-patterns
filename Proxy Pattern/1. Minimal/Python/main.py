from proxy_subject import ProxySubject

def main():
    print("Proxy Pattern in Python")
    print("-----------------------")
    print()

    print("Create proxy instance.")
    subject = ProxySubject()

    print("Call proxy doSomething method.")
    subject.doSomething()
    print("Call proxy doSomething method again.")
    subject.doSomething()

if __name__ == "__main__":
    main()
