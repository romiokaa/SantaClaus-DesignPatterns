class Workshop:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)