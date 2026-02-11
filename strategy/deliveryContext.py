class DeliveryContext:
    def __init__(self, delivery):
        self.delivery = delivery

    def execute(self):
        return self.delivery.deliver()