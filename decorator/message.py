from .giftDecorator import GiftDecorator

class Message(GiftDecorator):
    def __init__(self, gift, text):
        super().__init__(gift)
        self.text = text

    def description(self):
        return self.gift.description() + f" with message '{self.text}'"