class Elf:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Elf {self.name} notified: {message}")