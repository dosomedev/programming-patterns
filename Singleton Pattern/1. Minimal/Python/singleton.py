class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def setMessage(self, message):
        self._message = message

    def showMessage(self):
        print(self._message)
