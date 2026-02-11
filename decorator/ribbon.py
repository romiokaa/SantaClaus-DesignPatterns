from .giftDecorator import GiftDecorator

class Ribbon(GiftDecorator):
    def description(self):
        return self.gift.description() + " with ribbon"