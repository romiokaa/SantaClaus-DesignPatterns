from .giftDecorator import GiftDecorator

class GiftWrap(GiftDecorator):
    def description(self):
        return self.gift.description() + " wrapped"