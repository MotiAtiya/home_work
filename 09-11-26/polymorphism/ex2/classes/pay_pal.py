from .payment_method import PaymentMethod

class PayPal(PaymentMethod):
    def pay(self, amount):
        return "Redirecting to PayPal " + str(amount)
    