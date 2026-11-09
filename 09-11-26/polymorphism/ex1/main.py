from classes.credit_card import CreditCard
from classes.pay_pal import PayPal

def checkout(pay_method, amount):
    return pay_method.pay(amount)


for method in [CreditCard(), PayPal()]:
    print(checkout(method, 100))
