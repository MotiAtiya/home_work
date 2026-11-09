from .payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    FEE = 0.02
    def pay(self, amount):
        return "Charging card " + str(amount)

    def fee(self, amount):
        return amount * CreditCard.FEE
