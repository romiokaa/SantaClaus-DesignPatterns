class GiftDecorator: 
    def __init__(self, gift):
        self.gift = gift

    def description(self):
        return self.gift.description()