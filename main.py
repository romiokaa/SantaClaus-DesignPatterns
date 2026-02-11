from facade.santaClausFacade import SantaClausFacade
from command.giftOrderCommand import GiftOrderCommand
from strategy.droneDelivery import DroneDelivery

def main():
    santaclaus = SantaClausFacade()

    giftOrder = GiftOrderCommand(santaclaus)

    giftOrder.execute("toy", DroneDelivery())

if __name__ == "__main__":
    main()
    