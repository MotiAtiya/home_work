from classes.credit_card import CreditCard
from classes.pay_pal import PayPal
from classes.apple_pay import ApplePay

def checkout(pay_method, amount):
    return str(pay_method.pay(amount)) + " | fee: " + str(pay_method.fee(amount))


for method in [CreditCard(), PayPal(), ApplePay()]:
    print(checkout(method, 100))
