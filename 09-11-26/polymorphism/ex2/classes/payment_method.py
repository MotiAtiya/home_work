class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("you must implement pay method")

    def fee(self, amount):
        return 0