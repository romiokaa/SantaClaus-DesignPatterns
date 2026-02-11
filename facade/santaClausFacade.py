from factory.giftFactory import GiftFactory
from observer.elf import Elf
from observer.workshop import Workshop
from decorator.giftWrap import GiftWrap
from decorator.ribbon import Ribbon
from decorator.message import Message
from strategy.deliveryContext import DeliveryContext

class SantaClausFacade:
    def __init__(self):
        self.factory = GiftFactory()
        self.workshop = Workshop()
        self.workshop.register(Elf("Antonella"))
        self.workshop.register(Elf("Patito"))

    def prepare_and_deliver_gift(self, gift_type, delivery_strategy):
        gift = self.factory.create_gift(gift_type)

        gift = GiftWrap(gift)
        gift = Ribbon(gift)
        gift = Message(gift, "Aquí mandan Las Divinas !")

        description = gift.description()

        self.workshop.notify(description)

        print(description)
        strategy = DeliveryContext(delivery_strategy).execute()
        print(strategy)






