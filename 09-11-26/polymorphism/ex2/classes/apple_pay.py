from .payment_method import PaymentMethod

class ApplePay(PaymentMethod):
    def pay(self, amount):
        return "Paid with Apple Pay " + str(amount)
