from .payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return "Charging card " + str(amount)
